---
author: Anthony Scotti
date: 2012-03-03T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Howto
- MongoDB
- Ruby
- Sinatra
title: MongoMapper with Sinatra Example
url: /2012/03/03/mongomapper-with-sinatra-example/
---

If you have worked with Ruby on Rails Activerecord before you know how it makes working with databases very easy by giving you objects to deal with communication with the database. [MongoMapper](http://mongomapper.com/) is an Object-Document-Mapper (ODM), it takes a lot of ideas from Activerecord and in turn should be very familiar. I found MongoMapper a good fit for people that want to use Sinatra ,because you are able to simply make your model classes right within the application file. MongoMapper will also work within Rails too if that's more like your style.

I coded up a small example of using MongoMapper with Sinatra to make a URL Shortener. Very rough but again is just an example.

{{< gist amscotti 2286860 >}}

Due to MongoDB being schema-less there is no need for database migrations, just ensure you have your database up and running and you should be good to go. The MongoMapper model is up top, named 'Shorten' consisting of variables for url, shorten_id, created_at and a count. This would become a collection within the database. Within the configure block, we tell MongoMapper what database to use, in this case 'urls'

If MongoMapper turns out not to be your cup of tea then you should take a look at [Mongoid](http://mongoid.org/), which could be a better fit. Both MongoMapper and Mongoid are able to be used within Rails but people say that [Mongoid](http://mongoid.org/) has better Rails 3 support.

After reading some postings and working with MongoDB you maybe wondering if there are any hosted solutions. There are 2 that come to mind, [MongoLab](https://mongolab.com) and [MongoHQ](https://mongohq.com/home). Both have a free tier to help you get started. Both are also available as add-ons from Heroku with great documentation which will make it easy to setup your application.

Here are some resources links,

*  [Mongomapper.com Documentation](http://mongomapper.com/documentation/)
*  [Rails Cast MongoDB and MongoMapper](http://railscasts.com/episodes/194-mongodb-and-mongomapper)
*  [Mongoid vs MongoMapper: Two Great MongoDB Libraries for Ruby](http://www.rubyinside.com/mongoid-vs-mongomapper-two-great-mongodb-libraries-for-ruby-3432.html)

If you have any questions or comments please post, also any suggestions on improving this are welcome.
