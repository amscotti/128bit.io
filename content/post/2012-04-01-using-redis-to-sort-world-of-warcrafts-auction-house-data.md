---
author: Anthony Scotti
date: 2012-04-01T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- API
- Howto
- JSON
- Redis
- Ruby
- Wow
- YAJL
title: Using Redis to sort World of Warcraft's Auction House data
url: /2012/04/01/using-redis-to-sort-world-of-warcrafts-auction-house-data/
---

If you have read some of my other postings you know by now that I enjoy using the data from World of Warcraft in my projects. In my mind it's a good amount of data that I can easily understand having played World of Warcraft for many years now. If you look at the [Blizzard Community Platform API Documentation](http://blizzard.github.com/api-wow-docs/#id3381986) you will see that there is an Auction Resource that will return a link to a JSON file you can download that will show you all the auctions for a given server. I wanted to be able to take this file and pull some useful data or format it in a way that I could easily push it into a database.

For the Lothar server, the file is about 4M, so I wanted to ensure that the JSON parse I was using is fast. From Google I found [yajl-ruby](https://github.com/brianmario/yajl-ruby) which is "~1.9x faster than JSON.parse" which will help with reading the file. I also wanted to use [Redis](http://redis.io/) for this project. Redis isn't something that I have talked about a lot on the blog before but it's one of my favorite database systems. At its core it's a key-value data store but it also comes with a lot of other great features like, other data type like sets, sorted sets and hashes along with a [pubsub](http://redis.io/topics/pubsub) system. For this project I'm going to be using sets and sorted sets.

The idea of using Redis to sort data is one I got from Eric Redmond's talk on "[A CouchDB, Neo4j, Redis, and Node.JS Circus](http://www.livestream.com/nodepdx/video?clipId=pla_84d1391f-49c6-4a54-b25a-c9c54028c93c)" from NodePDX. It's a great talk about using a nice blend of technology or a nice list of buzz words! :)

Lets take a look at the code,

{{< gist amscotti 2278219 >}}

At the star it's reading the JSON return to get the URL for the main JSON file with all the auction data. Next we parse the auction data and start loading the auctions for the alliance (only loading in the alliance data for I can easily check it). Redis's sorted sets take use of 3 keys, the item ID as the key, the bid as the score and the auction ID as the unique key. Redis will sort the data as it goes in to the database based on the score or the bid price. I also add the item ID to a set for I can easily iterate over all the data that was loaded from the JSON file.

The next part reads back the data, for each item in the set I find top and bottom item or the lowest and highest price and then return its score or price. I divide by 10000 as all the price are in copper and it's easier to read them in gold. If you wanted the output to be in Gold, Silver and Copper then you can use divide with modulo operation to do this.

I also wanted to display the item name not just the ID, there is another API call for this but doing a call per item takes a long time so I use Redis to build up a local cache of the names. When you do a get on a key that is not in the database Redis will return nil. If the name is nil then I make a API call to get the name and then I save it back in to the database. Next time around the key isn't nil and I don't need to make the API call. I did find that two items where missing from the API and would reply with a HTTP 404 error. Not sure why they are missing but here are the ones I found, 39998 is Brilliant Scarlet Ruby and 41782 is Design: Lightning Forest Emerald, I just looked them up on [Wowhead](http://www.wowhead.com) and added them to the database by hand. Just keep this in mind when running the code.

The output will show the lowest and highest bids on a item along with how many items. The output is just there to show something from the code, I see this being used as a step to get data into a other type of database.

If you have any questions or comments please post, also any suggestions on improving this are welcome.
