Title: Playing around with LevelDB
Date: 2014-03-23 00:00
Slug: 2014/03/23/playing-around-with-leveldb
Save_as: 2014/03/23/playing-around-with-leveldb/index.html
URL: 2014/03/23/playing-around-with-leveldb/
Tags: LevelDB, noSQL, Google
Summary: An introduction to Google's LevelDB, an on-disk key-value store based on BigTable concepts without sharing code. Covers using LevelDB embedded or as backend storage like Riak, its multi-level architecture for performance through tiered data storage, typical use cases, and being found in Chrome's IndexedDB implementation.

![LevelDB Logo](/images/logo/leveldb.png)

If you have looked over a number of my postings,  you can tell that I enjoy playing around with noSQL databases but for this posting I wanted to look at something a bit lower level.

LevelDB is a on-disk key/value store that is written by Google. It's based on concepts from [Google's BigTable](http://en.wikipedia.org/wiki/BigTable) database system without sharing any of the code. You can think of LevelDB in the same way as something like SQLite. It is typically embedded into applications or used as the back end storage to pre-existing databases, like [Riak](http://basho.com/riak/) for example. You can also find it as part of Google's Chrome browser for their implantation of IndexedDB for client-side storage.

LevelDB get it's name for the way it stores the data into different levels. Data is first pushed into the log level and as time goes by the data is moved into deeper levels. Here is an idea of how the levels would look.

* Log: Max size of 4MB, then flushed into a set of Level 0 SST files
* Level 0: Max of 4 SST files, then one file compressed into Level 1
* Level 1: Max total size of 10MB, then one file compressed into Level 2
* Level 2: Max total size of 100MB, then one file compressed into Level 3
* Level 3+: Max total size of 10 x previous level, then one file compressed into next level

More details can be found in [Google's leveldb documentation](http://leveldb.googlecode.com/svn/trunk/doc/impl.html)

All data that is put into LevelDB is automatically compressed by Google's [Snappy](https://code.google.com/p/snappy/) compression library to keep the size of your database down. Snappy doesn't optimize for compression size but it optimizes for speed.

## Commands
Being a key/value based store, the commands for working with LevelDB are simple to understand.

* put - Push an item into the database
* get - Get an item out of the database
* del - Remove an item from the database
* batch - Do many operations at the same time

If you have worked with any other key/value store their commands will look very familiar to you. There is also support for forward and backward iteration over your keys.

## Using from NodeJS
As LevelDB does not provide any server or command-line interface, it must be used from within an application. There are drivers for using LevelDB in just about any language you may want to, but NodeJS seems to have a great integration for LevelDB.

To use from NodeJS I used a library called level, which is both LevelUp and LevelDown together.

I put together a small project, it's a url shortener. Nothing special by any means but does demonstrate the use of level along with Q for promised based callbacks. The project can be found here: [https://github.com/amscotti/urlLeveler](https://github.com/amscotti/urlLeveler)

## Ideas for using LevelDB
One of the things to keep in mind is that LevelDB is single threaded, which means it cannot be connected from two separate processes. It is meant to be used by one application at a time. At first glance you may think that this is pointless but there are still a lot of uses for this type of database.

If you quickly want to add a layer of caching to your application you could easily do this by using LevelDB.

If you're digesting data from a firehose at a rapid rate, you could use LevelDB as a buffer for the data before you process it.

Primarily LevelDB is meant to be built upon, you could easily build your own database system using LevelDB.

For some other ideas, checkout this video "[Julian Gruber: Level Me up Scotty!](http://www.youtube.com/watch?v=41oDDTRWjIQ)"

## Resources
* [LevelDB Home Page](https://code.google.com/p/LevelDB/)
* [DailyJS: LevelDB and Node: What is LevelDB Anyway?](http://dailyjs.com/2013/04/19/LevelDB-and-node-1/)
* [LevelDB - The Node.js of Databases - Rod Vagg](http://coderead.wordpress.com/2013/04/04/node-js-LevelDB/)
