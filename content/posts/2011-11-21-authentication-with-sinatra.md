Title: Authentication with Sinatra
Date: 2011-11-21 00:00
Slug: 2011/11/21/authentication-with-sinatra
Save_as: 2011/11/21/authentication-with-sinatra/index.html
URL: 2011/11/21/authentication-with-sinatra/
Tags: Howto, Ruby, Sinatra
Summary: A Sinatra authentication example using sessions, BCrypt for password hashing with salts, and HAML templates. Demonstrates signup/login flow with in-memory user storage for prototyping, showcasing Sinatra's simplicity for building micro web apps suitable for hosting on platforms like Heroku.

One of the things I'm heavily looking in to is [Sinatra](http://www.sinatrarb.com), it's a micro-web framework which I feel gives you more freedom over your project and lets you rapidly prototype things out. You are able to keep a full app in one file which is perfect for use with Github's Gist. Sinatra lets you quickly build web apps in a short amount of time with less complexity then a Rails app. A lot of places that host Rails apps will also host Sinatra apps using Rack. A place where I plan on releasing one of my projects is [Heroku](http://www.heroku.com). They are willing to give you a free web node, for small apps this will do fine and if later on you need to scale up it's easy to do.

I couldn't find any clear way of doing authentication within a Sinatra app so I made up some code that I hope will give people an idea on how to start.

```ruby
require 'rubygems'
require 'bcrypt'
require 'haml'
require 'sinatra'

enable :sessions

userTable = {}

helpers do

  def login?
    if session[:username].nil?
      return false
    else
      return true
    end
  end

  def username
    return session[:username]
  end

end

get "/" do
  haml :index
end

get "/signup" do
  haml :signup
end

post "/signup" do
  password_salt = BCrypt::Engine.generate_salt
  password_hash = BCrypt::Engine.hash_secret(params[:password], password_salt)

  #ideally this would be saved into a database, hash used just for sample
  userTable[params[:username]] = {
    :salt => password_salt,
    :passwordhash => password_hash
  }

  session[:username] = params[:username]
  redirect "/"
end

post "/login" do
  if userTable.has_key?(params[:username])
    user = userTable[params[:username]]
    if user[:passwordhash] == BCrypt::Engine.hash_secret(params[:password], user[:salt])
      session[:username] = params[:username]
      redirect "/"
    end
  end
  haml :error
end

get "/logout" do
  session[:username] = nil
  redirect "/"
end

__END__
@@layout
!!! 5
%html
  %head
    %title Sinatra Authentication
  %body
  =yield
@@index
-if login?
  %h1= "Welcome #{username}!"
  %a{:href => "/logout"} Logout
-else
  %form(action="/login" method="post")
    %div
      %label(for="username")Username:
      %input#username(type="text" name="username")
    %div
      %label(for="password")Password:
      %input#password(type="password" name="password")
    %div
      %input(type="submit" value="Login")
      %input(type="reset" value="Clear")
  %p
    %a{:href => "/signup"} Signup
@@signup
%p Enter the username and password!
%form(action="/signup" method="post")
  %div
    %label(for="username")Username:
    %input#username(type="text" name="username")
  %div
    %label(for="password")Password:
    %input#password(type="password" name="password")
  %div
    %label(for="checkpassword")Password:
    %input#password(type="password" name="checkpassword")
  %div
    %input(type="submit" value="Sign Up")
    %input(type="reset" value="Clear")
@@error
%p Wrong username or password
%p Please try again!
```

Again, the hash is used in place for a database just for the sample. You really want to replace this with some database back-end.

If you see anyway of making this code better please comment or fork the Gist
