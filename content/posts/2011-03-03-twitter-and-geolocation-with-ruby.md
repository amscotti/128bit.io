Title: Twitter and Geolocation with Ruby
Date: 2011-03-03 00:00
Slug: 2011/03/03/twitter-and-geolocation-with-ruby
Save_as: 2011/03/03/twitter-and-geolocation-with-ruby/index.html
URL: 2011/03/03/twitter-and-geolocation-with-ruby/
Tags: Geolocation, Howto, Ruby, Twitter
Summary: A Ruby example demonstrating how to pull friend data from Twitter API and use Geokit gem to geocode their profile locations. Code retrieves friends list, checks for location data, queries Yahoo's Geocoding API for coordinates, noting API rate limits and that profile locations may not reflect actual posting locations.

It goes without saying that there is TONS of data on Twitter, luckily there is a nice API to be able to read some of that data. There are a good number of apps annd sites that are using this data and making some great services that help with analyzing, sorting, and parsing content from other social networks. So I wanted to take a quick look at what it takes to read some data from the Twitter API from Ruby and write a little fun code that also does some Geolocation based on your friends location they enter on Twitter.

Not a new idea at all, [pleaserobme.com](https://cdt.org/blog/over-sharing-and-location-awareness/) was tracking Geo data from Twitter and Foursquare to tell everbody when you where not home. It was to make people aware of how much data they are sharing online. They shortly stopped after starting as they were _"...satisfied with the attention we've gotten..."_, the site is no longer maintained.

Another Twitter and Geo site mashup is [trendsmap.com](http://trendsmap.com), this is a nice site for seeing trends on a map. Can be used to see whats happing around the world based off what people are saying on Twitter. Seems like a cool idea and I can see some marketing usefulness around it.

The Twitter API is REST based that returns JSON data back, so any languages that are able to make REST calls and decode JSON data should be able to use the Twitter API but I wanted to cheat abit and use a Ruby Gem to make my life easier. I chose to use the [Twitter gem by John Nunemaker](http://twitter.rubyforge.org/). As it seems to be the most used Twitter gem around... (also the first that showed up on Google). One thing to keep in mind when using the Twitter API is the number of calls you can make, 150 requests per hour and 350 OAuth'ed requests per hour. Because this is just me playing around with the API, I don't really care too much about how the Gem connects to the API and how many calls the API makes per Ruby call. If I was working on a app for work I can see myself writing out API calls myself or looking into the Gem to make sure there were no wasted API calls.

For the Geolocation part of the code I'm going to use the [Geokit](http://geokit.rubyforge.org/) gem. This gem seems to be maintained and recently updated than the others I looked at. It uses both Google's and Yahoo's API for Geolocation which from my testing seem to return about the same info.

Based on your OS you should be able to run something like this to install the gems,
`gem install twitter geokit`
and here is the code.

```ruby
require "rubygems"
require "twitter"
require 'geokit'

username = "amscotti"

friends_list = Twitter.friends(username)
friends_list.users.each do |friend|
  puts "----------------------------"
  unless friend.location.nil? || friend.location.strip.empty?
    puts "#{friend.name} AKA #{friend.screen_name} is from #{friend.location}"
    geo = Geokit::Geocoders::YahooGeocoder.geocode(friend.location)
    puts geo.success ? "#{geo.lat}, #{geo.lng}" : "Unable to find Geo for #{friend.location}"
  else
    puts "#{friend.name} AKA #{friend.screen_name} idk where they are from..."
    puts "No listed location"
  end
end
```

Keep in mind this isn't getting Geo data from their posting, this is the info they have entered for their profile location and because of this it may not be truthful, right or even filled out. I would say the next steps would be to map out this data in some way in a Google Map. I may also write some code that would look at the Geo data from the postings themselves and map them out. Sadly a lot of people don't have Geo turned on when they are posting.

If you have any questions or comments please post, also any suggestions on improving this are welcome.
