Title: DynamoDB, Amazon's scalable NoSQL database
Date: 2012-06-28 00:00
Slug: 2012/06/28/dynamodb-amazons-scalable-nosql-database
Save_as: 2012/06/28/dynamodb-amazons-scalable-nosql-database/index.html
URL: 2012/06/28/dynamodb-amazons-scalable-nosql-database/
Tags: AWS, DynamoDB, noSQL, Opinion, Review
Summary: A review of Amazon DynamoDB key-value database service. Compares to SimpleDB, explains Dynamo's white paper origins and influences on Cassandra and Riak, highlights predictability of performance with configurable throughput, discusses trade-offs like 64KB item limit and lack of easy table cloning, and praises ease of setup over self-administered NoSQL databases.

One of the things that really gets me excited about my new job is being able to use new technology. Sure, sometimes new technology is risky but I see groups befitting more then failing due to using newer technology. As always when talking about new technology, NoSQL seems to come up because there are a good number of people switching parts (or all) of their application to use NoSQL databases to get by limits or to help with scalability issues. And here comes Amazon to the rescue with another database service.

At this point in time there are 3 types of database services you can get from Amazon. Relational Database Service (RDS) is your traditional database like MySQL, Oracle and SQL Server. Nothing really out of the ordinary here, we have all been using these for years. The only difference is they are in the "Cloud" managed by Amazon.

The last two database services are [SimpleDB](http://aws.amazon.com/simpledb/) and [DynamoDB](http://aws.amazon.com/dynamodb/). Amazon SimpleDB is a NoSQL database, but compared to DynamoDB this has many limitations as far as performance and scaling. Even though there are limitations it is nice that SimpleDB will make indexes of all attributes for each item stored. This is something that you are unable to do in DynamoDB. I feel that SimpleDB showed Amazon that people would use a NoSQL database service in the cloud. I truthfully have never used SimpleDB, so I can't speak much more about it. I also have a feeling that DynamoDB will replace SimpleDB over time.

Amazon's solution to some of the limitations with SimpleDB is DynamoDB. DynamoDB is a key-value store that is highly available. The idea of Dynamo comes from a [white paper written by Amazon](http://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf) talking about the system they had used inhouse for Amazon.com. No code was released just the idea, similar to what [Google did for Big table](http://research.google.com/archive/bigtable.html). From Amazon's paper, people did make their own Dynamo inspired databases systems, [Cassandra](http://en.wikipedia.org/wiki/Apache_Cassandra) and [Riak](http://en.wikipedia.org/wiki/Riak) are the two that I know of. Now Amazon is offering their own Dynamo based database which is highly available, along with predictable performance.

With all 3 database services we have the idea of removing operational needs (sorry Admins... we don't need you anymore) along with having a distributed system at your fingertips. A lot more details can be found on [Werner Vogels blog](http://www.allthingsdistributed.com/2012/01/amazon-dynamodb.html) of the history of NoSQL at Amazon.

With all NoSQL databases I feel they have a gimmick to them to separate themselves from the rest of the pack. There are a good number of key-value databases out there, why go with DynamoDB? Like a lot of Amazon Web Services they are easy to setup and to start working with. All you have to do is log on to AWS and make a table. The other big thing you get is predictability of performance. If you have [watched the video](http://www.youtube.com/watch?v=oz-7wJJ9HZ0) they made, one of the key points is being able to scale based on your needs of read/write throughput (using yummy Solid State Drives!) along with Amazon dealing with the replication and [sharding](http://en.wikipedia.org/wiki/Shard_%28database_architecture%29) needed to scale NoSQL databases.

As with most things in real life, when you gain something you often have to give up something. Due to the nature of key-value databases, you really need to think ahead of how you want to use your data because you can only really do look ups on your keys. One nice thing that DynamoDB adds is a range key that you can do look ups along with your hash key. This gives you a bit more flexibility when you do your look ups. Also, as a developer you need to take care of what you are doing or you may end up increasing your cost due to the way you are pulling data. There is also a 64KB limit in place for the size of an item which means if you are moving data into DynamoDB you may have to change your schema around to keep your items under 64KB. With this trade off Amazon is able to give you predictability of performance that lets you scale based on your needs. For some people this will work out just fine but for others their limitations will make it hard.

DynamoDB is still in beta so there are some nice things that seem to be missing. Over time I see Amazon adding them but for now there seems to be no easy way to backup your data besides using Elastic MapReduce. Also, there seems so be no way to easily clone a table. This would be a great way to do testing or debugging if you could just clone a production table, work out any issues using real data, then just drop the table when you are done.

For my projects that I have been using DynamoDB on, it's been a good fit and given some nice advantages along with ease of development. Somethings have been tricky to get my head around but overall I enjoy using DynamoDB. I'm still partial to other NoSQL technologies but not needing to setup and admin a scalable database system is a huge plus in my book!

I'm hoping to have some code examples in another posting about using DynamoDB along with what it takes to layout tables to be able to pull data.

## Here are some resources links:
* [Webinar: Amazon Dynamo DB](http://www.youtube.com/watch?v=meBjA68DeIU&feature=relmfu)
* [Amazon DynamoDB - What's It All About?](http://www.youtube.com/watch?v=nMhWJJACZSA&feature=relmfu)
* [Amazon DynamoDB Developer Guide](http://www.amazon.com/Amazon-DynamoDB-Developer-Guide-ebook/dp/B007Q4JGBM)
