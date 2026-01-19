Title: Updated World of Warcraft Armory code
Date: 2011-09-22 00:00
Slug: 2011/09/22/updated-world-of-warcraft-armory-code
Save_as: 2011/09/22/updated-world-of-warcraft-armory-code/index.html
URL: 2011/09/22/updated-world-of-warcraft-armory-code/
Tags: API, CoffeeScript, Groovy, Howto, REST, Ruby, Wow
Summary: Updated code for pulling World of Warcraft character data from Battle.net's new REST API returning JSON. Includes solutions in Ruby using HTTParty, Groovy with JSON slurper, and CoffeeScript running on Node.js, replacing older XML-based approaches that broke when Battle.net upgraded their armory.

I haven't been playing World of Warcraft for a bit, but I guess they did some big updates to the armory which stopped the code I had written before from running correctly. (Link to the old code, [Ruby](/2010/05/09/ruby-and-armory/) and [Groovy](/2010/06/03/pulling-data-from-the-warcraft-armory-with-groovy/))

After looking in to what has changed, I found out they added a new [REST API](http://en.wikipedia.org/wiki/Representational_state_transfer) for Battle.net which lets you pull data easily without the need of tricking the server to pass you XML. From the API, we get nice JSON data to work with. So here is some new code in Ruby, Groovy and CoffeeScript (running on [Node.js](http://nodejs.org/)) that can be used to get about the same output as the code I had before. ([Link to gist](https://gist.github.com/1236553))

### Ruby
```ruby
require 'rubygems'
require 'httparty'

type = {
  1 => "Warrior", 2 => "Paladin", 3 => "Hunter",
  4 => "Rogue", 5 => "Priest", 6 => "Death Knight",
  7 => "Shaman", 8 => "Mage", 9 => "Warlock",
  10 => "Monk", 11 => "Druid"
}
type.default = "unknown"

strRealm = "Staghelm"
strGuildName = "Controlled Chaos"

data = HTTParty.get("http://us.battle.net/api/wow/guild/#{URI.escape(strRealm)}/#{URI.escape(strGuildName)}?fields=members").parsed_response
puts "#{data["members"].count} Characters Found!"
puts "-" * 50
data["members"].sort{|a,b| a["character"]['name'] <=> b["character"]['name']}.each do |member|
  c = member["character"]
  puts "%-20s%-10s%s" %[c['name'],c['level'],type[c['class']]]
end
puts "-" * 50
```

### Groovy
```groovy
import groovy.json.*

def realm = URLEncoder.encode("Staghelm")
def guild = URLEncoder.encode("Controlled Chaos").replace("+", "%20")

def url = "http://us.battle.net/api/wow/guild/${realm}/${guild}?fields=members".toURL()

def type = [
1: "Warrior",    2: "Paladin",     3: "Hunter",
4: "Rogue",      5: "Priest",      6: "Death Knight",
7: "Shaman",     8: "Mage",        9: "Warlock",
10: "Monk",     11: "Druid"].withDefault { key -> "unknown" }

url.openConnection().with {
    inputStream.withReader { reader ->
        def characters = new JsonSlurper().parse(reader)
        println "${characters.members.size} Characters Found!"
        println "-" * 50
        characters.members.character.sort{ it.name }.each { t ->
          printf "%-20s%-10s%s\n", t.name, t.level, type[t.class]
        }
        println "-" * 50
    }
}
```

### CoffeeScript
```coffeescript
http = require 'http'
rest = require 'restler'

realm = escape "Staghelm"
guild = escape "Controlled Chaos"

type = {
  1: "Warrior",    2: "Paladin",     3: "Hunter",
  4: "Rogue",      5: "Priest",      6: "Death Knight",
  7: "Shaman",     8: "Mage",        9: "Warlock",
  10: "Monk",     11: "Druid"
}

rest.get("http://us.battle.net/api/wow/guild/#{realm}/#{guild}?fields=members").on('complete', (data) ->

  data.members.sort( (a,b) ->
    if a.character.name > b.character.name
      return 1
    if a.character.name < b.character.name
      return -1
    return 0
  )

  console.log "#{data.members.length} Characters Found!"
  console.log "--------"
  for char in data.members
    console.log "#{char.character.name} #{char.character.level}  #{type[char.character.class]}"
  console.log "--------"
)
```


For more info on the Battle.net API check out the [API Documentation](http://blizzard.github.com/api-wow-docs/)

If you have any questions or comments please post, also any suggestions on improving this are welcome as I'm sure there are ways to improve the code.
