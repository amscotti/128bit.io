---
author: Anthony Scotti
date: 2012-01-29T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Howto
- MongoDB
- noSQL
title: Getting started with MongoDB
url: /2012/01/29/getting-started-with-mongodb/
---

I'm a big fan of CouchDB. I enjoy how they go about doing things and how you are able to use it without the need of drivers as its all RESTful based. As long as your language of choice has the ability to make RESTful calls and read JSON data then you're all set. But before I really started to use CouchDB I did start looking at MongoDB, another Document data store. MongoDB is now being compared to mySQL as far as its use by projects. It has a great group of developers along with getting some great press from big companies moving over to MongoDB from some type of SQL based system.

I wanted to take another look at MongoDB and eventually do some playing around with it in Ruby for another posting.
## Installing
You can get MongoDB from their download page at [http://www.mongodb.org/downloads](http://www.mongodb.org/downloads), for MacOS, I installed it the same way for these types of apps.
```
$ wget http://fastdl.mongodb.org/osx/mongodb-osx-x86_64-2.0.2.tgz
$ tar -xzf mongodb-osx-x86_64-2.0.2.tgz
$ sudo mv mongodb-osx-x86_64-2.0.2 /usr/share/
$ cd /usr/share/
$ sudo ln -s mongodb-osx-x86_64-2.0.2/ mongodb
$ sudo mkdir -p /data/db
```
Don't forget the last part, /data/db is the path where your databases are saved. After moving around the files be sure to add lines below to your .profile in your home folder.
```
MONGODB_HOME=/usr/share/mongodb; export MONGODB_HOME
PATH=$MONGODB_HOME/bin:$PATH; export PATH
```

Now lets test it out. First we need to start the server and then run the clients for it.
```
$ sudo mongod
mongod --help for help and startup options
Tue Jan 17 13:20:47 [initandlisten] MongoDB starting : pid=3072 port=27017 dbpath=/data/db/ 64-bit host=Lycan.local
Tue Jan 17 13:20:47 [initandlisten] db version v2.0.2, pdfile version 4.5
Tue Jan 17 13:20:47 [initandlisten] git version: 514b122d308928517f5841888ceaa4246a7f18e3
Tue Jan 17 13:20:47 [initandlisten] build info: Darwin erh2.10gen.cc 9.6.0 Darwin Kernel Version 9.6.0: Mon Nov 24 17:37:00 PST 2008; root:xnu-1228.9.59~1/RELEASE_I386 i386 BOOST_LIB_VERSION=1_40
...
```
and now in a new shell start the client,
```
$ mongo
MongoDB shell version: 2.0.2
connecting to: test
>
```
At this point you are all set to start playing around with the database. There are also [downloads](http://www.mongodb.org/downloads) for Linux, Windows and Solaris along with packages for [Ubuntu](http://www.mongodb.org/display/DOCS/Ubuntu+and+Debian+packages) and [Fedora](http://www.mongodb.org/display/DOCS/CentOS+and+Fedora+Packages).

## Some playing around
Now that we have everything all set, lets play around in the client. This is a Javascript base client and documents are JSON data, so if you have worked with JSON before you should be familiar. Sadly there is no web interface like the one that comes with CouchDB, but you can get a 3rd party one.
```
MongoDB shell version: 2.0.2
connecting to: test
> use playingaround
switched to db playingaround
> doc = {fname:"Anthony", lname:"Scotti", favcolor:"Blue"}
{ "fname" : "Anthony", "lname" : "Scotti", "favcolor" : "Blue" }
> db.mytest.save(doc)
> db.mytest.find()
{ "_id" : ObjectId("4f19f49c4bffc928bbeee802"), "fname" : "Anthony", "lname" : "Scotti", "favcolor" : "Blue" }
> db.mytest.save({fname:"Dave", lname:"Smith", favcolor:"Green"})
> db.mytest.find()
{ "_id" : ObjectId("4f19f49c4bffc928bbeee802"), "fname" : "Anthony", "lname" : "Scotti", "favcolor" : "Blue" }
{ "_id" : ObjectId("4f19f4f74bffc928bbeee803"), "fname" : "Dave", "lname" : "Smith", "favcolor" : "Green" }
> db.mytest.findOne()
{
	"_id" : ObjectId("4f19f49c4bffc928bbeee802"),
	"fname" : "Anthony",
	"lname" : "Scotti",
	"favcolor" : "Blue"
}
> db.mytest.findOne({fname:"Dave"})
{
	"_id" : ObjectId("4f19f4f74bffc928bbeee803"),
	"fname" : "Dave",
	"lname" : "Smith",
	"favcolor" : "Green"
}
>
```
So what's happening here?

The first line, 'connecting to: test' tells you that you have connected to the test database. The `use playingaround` is switching/making a new database for you. As far as the 'mytest', this is a collection, think of a collection like a table, it's what is going to hold the documents for you.

The next lines are making a document and saving it into a doc variable to be used later. As you can see it's JSON format, to save this in to the collection all you need to do is run `db.mytest.save(doc)`, where you would replace 'mytest' with your collection name.

The `.find()` and `.findOne()` will show you documents that are in the collection, `.findOne` will only show you one document at a time though you are able to pass in criteria in to the find like I did with the `.findOne({fname:"Dave"})`

This is a very quick overview of using the client, you can find much better info on [MongoDB.org's Tutorial](http://www.mongodb.org/display/DOCS/Tutorial) and [MongoDB.org's Overview](http://www.mongodb.org/display/DOCS/Overview+-+The+MongoDB+Interactive+Shell)

If you have any questions or comments please post, also any suggestions on improving this are welcome.
