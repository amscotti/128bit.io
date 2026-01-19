Title: Pulling data from the Warcraft Armory with Ruby
Date: 2010-05-09 00:00
Slug: 2010/05/09/ruby-and-armory
Save_as: 2010/05/09/ruby-and-armory/index.html
URL: 2010/05/09/ruby-and-armory/
Tags: Howto, Ruby, Wow, XML
Summary: A Ruby script demonstrating how to pull character data from the World of Warcraft Armory website. The code fetches XML from the armory, parses guild information, and extracts level 80 characters with their names, levels, and classes into a sorted list.

**Update:** New code using Battle.net's REST API can be found [here](/2011/09/22/updated-world-of-warcraft-armory-code/).


For the people that play World of Warcraft, you know there is a great site made by Blizzard that keeps all your characters and guild information called the armory. If you take a good look at the site you will see its XML being formatted by XSLT. This is really great for people that want to script something to pull data from the armory because XML is really easy to parse.

The idea of this code is to form the URL path and pull the XML to parse out the data we want. This code is just going to pull level 80s (max level at time of writing this) from a guilds list. You can take this further and start pulling data per character from that list but this is just to get you started. I am using Ruby because I'm trying to learn the ins and outs of it, but the same can be done in Python or any other languages that can handle downloading and parsing XML.

```ruby
require 'net/http'
require 'rexml/document'
include REXML

def get_xml_page(strRealm, strGuildName)
  oresp = Net::HTTP.start( "www.wowarmory.com") do |http|
    http.get( "/guild-info.xml?r=#{strRealm}&n=#{strGuildName}",
    { 'user-agent' => 'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-GB; rv:1.8.1.4) Gecko/20070515 Firefox/2.0.0.4'})
  end

  return oresp
end

def get_guild_info(xmlPage)
  str_max_level = '80'
  info_array = []

  odoc = REXML::Document.new xmlPage.body
  odoc.elements.each( '*//character') do |oElement|
    if oElement.attributes['level'] == str_max_level
      info_array << [oElement.attributes['name'],oElement.attributes['level'], oElement.attributes['classId']]
    end
  end

 return info_array
end

def get_class_name(classId)
  case classId
    when "1"
      return "Warrior"
    when "2"
      return "Paladin"
    when "3"
      return "Hunter"
    when "4"
      return "Rogue"
    when "5"
      return "Priest"
    when "6"
      return "Death Knight"
    when "7"
      return "Shaman"
    when "8"
      return "Mage"
    when "9"
      return "Warlock"
    when "11"
      return "Druid"
  else
   return "ERROR:#{classId}"
  end
end

str_realm = 'Staghelm'
str_guild_name = "Controlled+Chaos"

xml_page = get_xml_page(str_realm, str_guild_name)
character_list = get_guild_info(xml_page)

puts "#{character_list.length} Character Found!"
puts "-------------------------"
character_list.sort.each { |character| puts "%-20s%-10s%s" %[character[0],character[1],get_class_name(character[2])]}
puts "-------------------------"
```

This will out put a nice list of all the level 80 toons and their class that are within the guild.
I'm sure there is a better way to do this and I would love to know, so if you know please leave a comment. Feedback is welcome as well!
