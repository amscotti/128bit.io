Title: MongoDB, added Ruby in to the mix
Date: 2012-02-08 00:00
Slug: 2012/02/08/mongodb-added-ruby-in-to-the-mix
Save_as: 2012/02/08/mongodb-added-ruby-in-to-the-mix/index.html
URL: 2012/02/08/mongodb-added-ruby-in-to-the-mix/
Tags: Howto, MongoDB, noSQL, Ruby
Summary: Exploring MongoDB with Ruby using mongo driver for database operations. Demonstrates basic CRUD operations with MongoDB shell, connecting with Ruby, performing queries and updates, and noting similarities and differences to SQL databases in document-oriented storage approach.

To keep with the [previous posting I made with MongoDB](/2012/01/29/getting-started-with-mongodb/), I am going to show some Ruby code of how to connect and push data in to your database. If you take a look at the MongoDB driver page you see that there are a good number of programming languages that are supported by MongoDB.org along with tons that are supported by the community. My languages of choice is Ruby. It's a Supported language from MongoDB.org and you can install the drivers using gem.

There are 2 Gems you are going to want to install, 'mongo' and 'bson_ext', you are able to get away with installing just 'mongo'. You will be warned that any performance-critical applications should have 'bson_ext' installed. At this point you should be all set to start using MongoDB from Ruby. To give a quick overview, here is my Ruby World of Warcraft Armory code that dumps the data into MongoDB.

```ruby
require 'rubygems'
require 'nestful'
require 'mongo'

db = Mongo::Connection.new.db("wowstats")
coll = db.collection("character")
coll.drop

type = {
  	1 => "Warrior", 2 => "Paladin", 3 => "Hunter",
  	4 => "Rogue", 5 => "Priest", 6 => "Death Knight",
  	7 => "Shaman", 8 => "Mage", 9 => "Warlock",
  	11 => "Druid"
}
type.default = "unknown"

strRealm = "Lothar"
strGuildName = "Controlled Chaos"

data = Nestful.json_get "http://us.battle.net/api/wow/guild/#{URI.escape(strRealm)}/#{URI.escape(strGuildName)}?fields=members"

data["members"].each do |member|
  c = member["character"]
  doc = {:realm=>strRealm, :guild=>strGuildName, :name=>c['name'], :level=>c['level'], :class=>type[c['class']], :added=>Time.new}
  coll.save(doc)
end
puts "#{coll.count} Characters Found!"
puts "-" * 50
type.each_value do |type|
  puts "#{type}"
  puts "-" * 25
  coll.find({:class=>type}).sort([[:level, -1], [:name, 1]]).each do |c|
    puts "%-20s%-10s" %[c['name'],c['level']]
  end
  puts ""
end
puts "-" * 50
```

Not too many changes, we have at line 5 and 6 as the connection to the database and picking of the collection to be used. Line 7 isn't needed but if you keep running this code then you will keep on adding to the collection, by dropping it lets you remove all the data and start fresh. Line 24 and 25 are making a document as a hash and passing it to the collection to be save. You now have data in your MongoDB collection.

Now that we have data in the collection we are able to do some pulling. Line 27 shows us how many documents are in the collection. Line 32 is a find based on class type which is in a loop so all the classes will be looked up. All the other part of the code should be similar as before or just ruby code.

I hope to do another posting that shows off some code using MongoMapper which you can most likely guess from the name is an Object-relational mapping (ORM) for MongoDB.

If you have any questions or comments please post, also any suggestions on improving this are welcome.
