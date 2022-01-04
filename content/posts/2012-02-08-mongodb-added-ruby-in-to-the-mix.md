---
author: Anthony Scotti
date: 2012-02-08T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Howto
- MongoDB
- noSQL
- Ruby
title: MongoDB, added Ruby in to the mix
url: /2012/02/08/mongodb-added-ruby-in-to-the-mix/
---

To keep with the [previous posting I made with MongoDB]({{< relref "2012-01-29-getting-started-with-mongodb.md" >}}), I am going to show some Ruby code of how to connect and push data in to your database. If you take a look at the MongoDB driver page you see that there are a good number of programming languages that are supported by MongoDB.org along with tons that are supported by the community. My languages of choice is Ruby. It's a Supported language from MongoDB.org and you can install the drivers using gem.

There are 2 Gems you are going to want to install, 'mongo' and 'bson_ext', you are able to get away with installing just 'mongo'. You will be warned that any performance-critical applications should have 'bson_ext' installed. At this point you should be all set to start using MongoDB from Ruby. To give a quick overview, here is my Ruby World of Warcraft Armory code that dumps the data into MongoDB.

{{< gist amscotti 1650445 >}}

Not too many changes, we have at line 5 and 6 as the connection to the database and picking of the collection to be used. Line 7 isn't needed but if you keep running this code then you will keep on adding to the collection, by dropping it lets you remove all the data and start fresh. Line 24 and 25 are making a document as a hash and passing it to the collection to be save. You now have data in your MongoDB collection.

Now that we have data in the collection we are able to do some pulling. Line 27 shows us how many documents are in the collection. Line 32 is a find based on class type which is in a loop so all the classes will be looked up. All the other part of the code should be similar as before or just ruby code.

I hope to do another posting that shows off some code using MongoMapper which you can most likely guess from the name is an Object-relational mapping (ORM) for MongoDB.

If you have any questions or comments please post, also any suggestions on improving this are welcome.