Title: MongoMapper with Sinatra Example
Date: 2012-03-03 00:00
Slug: 2012/03/03/mongomapper-with-sinatra-example
Save_as: 2012/03/03/mongomapper-with-sinatra-example/index.html
URL: 2012/03/03/mongomapper-with-sinatra-example/
Tags: Howto, MongoDB, Ruby, Sinatra
Summary: An introduction to MongoMapper as an Object-Document-Mapper for MongoDB. Shows how to create model classes and use them within Sinatra applications, providing Active Record-like familiarity for database operations without the complexity of full Rails framework for micro applications.

If you have worked with Ruby on Rails Activerecord before you know how it makes working with databases very easy by giving you objects to deal with communication with the database. [MongoMapper](http://mongomapper.com/) is an Object-Document-Mapper (ODM), it takes a lot of ideas from Activerecord and in turn should be very familiar. I found MongoMapper a good fit for people that want to use Sinatra ,because you are able to simply make your model classes right within the application file. MongoMapper will also work within Rails too if that's more like your style.

I coded up a small example of using MongoMapper with Sinatra to make a URL Shortener. Very rough but again is just an example.

```ruby
require "rubygems"
require "sinatra"
require "haml"
require "mongo_mapper"

class Shorten
  include MongoMapper::Document

  key :url,        String
  key :shorten_id, String
  key :created_at, Time
  key :count,      Integer

end

configure do
  MongoMapper.database = 'urls'
end

get "/" do
  @shortens = Shorten.sort(:created_at.desc).limit(10)
  haml :index
end

post "/create" do
  @shorten = Shorten.where(:url=>params[:shorten][:url]).first
  if @shorten.nil?
    shorten_id = Shorten.all.count.to_s(16)
    @shorten = Shorten.new(:url=>params[:shorten][:url], :shorten_id=>shorten_id, :created_at=>Time.new, :count=>0)
    @shorten.save
  end
  redirect "/#{@shorten.shorten_id}/info"
end

get "/:id" do |id|
  @shorten = Shorten.where(:shorten_id=>id).first
  unless @shorten.nil?
    @shorten.count += 1
    @shorten.save
    redirect @shorten.url
  end
  redirect "/"
end

get "/:id/info" do |id|
  @shorten = Shorten.where(:shorten_id=>id).first
  if @shorten.nil?
    redirect "/"
  end
  haml :info
end

__END__
@@layout
!!! 5
%html
  %head
    %title Sinatra and MongoMapper Url Shortener
  %body
  =yield
@@index
%form{:action=>"/create", :method=>"post"}
  %div
    %label{:for=>"url"} URL:
    %input#url{:type=>"url", :placeholder=>"http://", :name=>"shorten[url]"}
  %div
    %input{:type=>"submit", :value=>"Submit"}
    %input{:type=>"reset", :value=>"Clear"}
#list{:style=>"margin-top: 20px;"}
  - @shortens.each do |shorten|
    %div
      %span.url{:style=>"margin-right: 50px;"}
        %a{:href=>"/#{shorten.shorten_id}"}= "#{shorten.url}"
      %span.count{:style=>"margin-right: 50px;"}= "#{shorten.count}"
      %span.info{:style=>"margin-right: 50px;"}
        %a{:href=>"/#{shorten.shorten_id}/info"} Info Page
@@info
%div
  %p= "URL: #{@shorten.url}"
  %p= "Shorten URL: http://#{request.host}/#{@shorten.shorten_id}"
  %p= "Created at: #{@shorten.created_at}"
  %p= "Count: #{@shorten.count}"
```

Due to MongoDB being schema-less there is no need for database migrations, just ensure you have your database up and running and you should be good to go. The MongoMapper model is up top, named 'Shorten' consisting of variables for url, shorten_id, created_at and a count. This would become a collection within the database. Within the configure block, we tell MongoMapper what database to use, in this case 'urls'

If MongoMapper turns out not to be your cup of tea then you should take a look at [Mongoid](http://mongoid.org/), which could be a better fit. Both MongoMapper and Mongoid are able to be used within Rails but people say that [Mongoid](http://mongoid.org/) has better Rails 3 support.

After reading some postings and working with MongoDB you maybe wondering if there are any hosted solutions. There are 2 that come to mind, [MongoLab](https://mongolab.com) and [MongoHQ](https://mongohq.com/home). Both have a free tier to help you get started. Both are also available as add-ons from Heroku with great documentation which will make it easy to setup your application.

Here are some resources links,

*  [Mongomapper.com Documentation](http://mongomapper.com/documentation/)
*  [Rails Cast MongoDB and MongoMapper](http://railscasts.com/episodes/194-mongodb-and-mongomapper)
*  [Mongoid vs MongoMapper: Two Great MongoDB Libraries for Ruby](http://www.rubyinside.com/mongoid-vs-mongomapper-two-great-mongodb-libraries-for-ruby-3432.html)

If you have any questions or comments please post, also any suggestions on improving this are welcome.
