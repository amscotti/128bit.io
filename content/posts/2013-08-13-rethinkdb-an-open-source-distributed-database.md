Title: RethinkDB, An Open-source Distributed Database
Date: 2013-08-13 00:00
Slug: 2013/08/13/rethinkdb-an-open-source-distributed-database
Save_as: 2013/08/13/rethinkdb-an-open-source-distributed-database/index.html
URL: 2013/08/13/rethinkdb-an-open-source-distributed-database/index.html
Tags: RethinkDB, noSQL
Summary: Review of RethinkDB as developer and operations oriented NoSQL database. Highlights JSON document storage, intuitive ReQL query language with joins, built-in MapReduce for distributed queries across cluster, easy web UI for administration and replication, strong official and community driver support, and potential for Spring Data integration.

As a developer I keep an eye on the noSQL space. I feel that noSQL truly empowers the developer to do more than using a relational database. They are typically easier to set up and to scale along with an ability to have a looser data structure which is able to evolve overtime. Don't get me wrong, relational databases have their place and will continue to be used many years from now, but just like using a new language or framework, developers can get a boost from using noSQL databases without having the restraints that come along with using a relational database.

### What is RethinkDB?

A couple weeks ago I stumbled upon RethinkDB, a noSQL database that is built to store JSON documents (like so many others) but also has an intuitive query language and simple administration along with a very nice web UI.

{% youtube qKPKsBNw604 %}

RethinkDB aims itself to be both Developer-oriented along with Operations-oriented. This means that Developers get a rich document structure along with flexible querying capabilities but the database is easy to deploy and scale. After setting up your systems, you can easily cluster them and use the web UI to start replicating and sharding your data over the systems with just a couple of clicks.

### Query language

RethinkDB comes with its own query language called 'ReQL'. The idea of a noSQL database having its own query language is nothing new if you have looked at other noSQL databases. Unlike other query languages you may find, this one is very intuitive and also has the ability to do Joins, which you don't find in many other noSQL databases.

Due to their query language, RethinkDB can be used to do some light analytics on your data. Under the hood, RethinkDB will use MapReduce to run your queries on all servers, the more systems you have in your cluster the more of a boost in performance.

Check out the [RethinkDB screencast](http://www.rethinkdb.com/screencast/) for a nice example of this using data from GitHub.

### Client drivers

RethinkDB has official drivers for JavaScript, Ruby, and Python. Along with the official drivers, there are community-supported drivers for many languages like Go, PHP, C#, Erlang, and Scala. The community drivers appear to follow a similar design to the official drivers. This I feel will make using RethinkDB easy from any language because all the APIs will be similar.

Beside the drivers, there are a good number of ORMs that you can use with RethinkDB, like [nobrainer](https://github.com/nviennot/nobrainer) for Ruby and [thinky](https://github.com/neumino/thinky) for JavaScript.

### Opinions

I think RethinkDB's focus is good, I feel that being Developer and Operations oriented is a huge win for everybody. I see RethinkDB being a good stepping stone into the noSQL world. The query language will not leave you missing much from SQL and your   Operations team will be thanking you for having a system that is easy to scale. I also see RethinkDB being a good companion database to other noSQL databases like Riak, Redis, and Neo4j to fulfill more specific tasks in your architecture.

One thing I would like to see is a Java Driver and a Spring Data abstraction, as much as I want to move away from Java it's still very much used all over the place and I think this would get more people using RethinkDB.

Over all I think RethinkDB is a database that should be looked at to see what other people have to offer in the noSQL space.

### Additional Resources
* [RethinkDB Home Page](http://www.rethinkdb.com)
* [RethinkDB Screencast](http://www.rethinkdb.com/screencast/)
* [RethinkDB example apps](http://www.rethinkdb.com/blog/rethinkdb-example-apps/)
* [Try RethinkDB](http://tryrethink.info/)
* [Reflection on RethinkDB](http://lethain.com/reflection-on-rethinkdb/)
* [RethinkDB Expands Beyond SSDs, Launches Its Speedy Database To The Public](http://techcrunch.com/2011/06/06/rethinkdb-expands-beyond-ssds-launches-its-speedy-database-to-the-public/)
