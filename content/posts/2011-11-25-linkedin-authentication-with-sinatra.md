Title: LinkedIn authentication with Sinatra
Date: 2011-11-25 00:00
Slug: 2011/11/25/linkedin-authentication-with-sinatra
Save_as: 2011/11/25/linkedin-authentication-with-sinatra/index.html
URL: 2011/11/25/linkedin-authentication-with-sinatra/
Tags: Howto, LinkedIn, Ruby, Sinatra
Summary: Sinatra example using linkedin gem for OAuth authentication and LinkedIn API access. Shows helper methods for login checking, profile retrieval, and connections listing with access tokens stored in sessions, adapted from Rails example for Sinatra's micro-framework simplicity.

To take the [authentication with Sinatra](http://www.128bitstudios.com/2011/11/21/authentication-with-sinatra) a bit farther you may want to use  another service to do your authentication against. This is some sample code adapted from a [Rails example](http://pivotallabs.com/users/will/blog/articles/1096-linkedin-gem-for-a-web-app). This code takes use of the [linkedin gem](https://github.com/pengwynn/linkedin) from [Wynn Netherland](http://wynnnetherland.com/) to do the authentication and also make some calls to the LinkedIn API. There are other gems that just do authentication for many services like Facebook and Twitter but for this sample I wanted to be able to make additional calls to the LinkedIn API.

```ruby
require "rubygems"
require "haml"
require "sinatra"
require "linkedin"

enable :sessions

helpers do
  def login?
    if session[:atoken].nil?
      return false
    else
      return true
    end
  end

  def profile
    unless session[:atoken].nil?
      client = LinkedIn::Client.new(settings.api, settings.secret)
      client.authorize_from_access(session[:atoken], session[:asecret])
      return client.profile
    end
  end

  def connections
    unless session[:atoken].nil?
      client = LinkedIn::Client.new(settings.api, settings.secret)
      client.authorize_from_access(session[:atoken], session[:asecret])
      return client.connections
    end
  end

end

configure do
  # get your api keys at https://www.linkedin.com/secure/developer
  set :api, "your_api_key"
  set :secret, "your_secret"
end

get "/" do
  haml :index
end

get "/auth" do
  client = LinkedIn::Client.new(settings.api, settings.secret)
  request_token = client.request_token(:oauth_callback => "http://#{request.host}:#{request.port}/auth/callback")
  session[:rtoken] = request_token.token
  session[:rsecret] = request_token.secret

  redirect client.request_token.authorize_url
end

get "/auth/logout" do
   session[:atoken] = nil
   redirect "/"
end

get "/auth/callback" do
  client = LinkedIn::Client.new(settings.api, settings.secret)
  if session[:atoken].nil?
    pin = params[:oauth_verifier]
    atoken, asecret = client.authorize_from_request(session[:rtoken], session[:rsecret], pin)
    session[:atoken] = atoken
    session[:asecret] = asecret
  end
  redirect "/"
end


__END__
@@index
-if login?
  %p Welcome #{profile.first_name}!
  %a{:href => "/auth/logout"} Logout
  %p= profile.headline
  %br
  %div= "You have #{connections.total} connections!"
  -connections.all.each do |c|
    %div= "#{c.first_name} #{c.last_name} - #{c.headline}"
-else
  %a{:href => "/auth"} Login using LinkedIn
```

If you know of any way to make this code better please comment or fork the Gist.
