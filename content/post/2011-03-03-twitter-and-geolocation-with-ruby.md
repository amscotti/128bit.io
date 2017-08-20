---
author: Anthony Scotti
date: 2011-03-03T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Geolocation
- Howto
- Ruby
- Twitter
title: Twitter and Geolocation with Ruby
url: /2011/03/03/twitter-and-geolocation-with-ruby/
---

It goes without saying that there is TONS of data on Twitter and luckily there is a nice API to be able to read some of that data within our code. There are a good number of apps/site that are taking use of this data and making some great services that help with analyzing, sorting along with parsing up content from other social networking. So I wanted to take a quick look at what it takes to read some data from the Twitter API from Ruby and write a little fun code that also does some Geolocation based on your friends location they enter on Twitter.

Not a new idea at all, for some time [pleaserobme.com](http://pleaserobme.com) was tacking Geo data from Twitter and Foursquare to tell everbody when you where not home. It was to make people aware of how much data they are sharing to online. They had to stop the pulling the day due being _"...satisfied with the attention we've gotten..."_.

Another Twitter and Geo site mashup is [trendsmap.com](http://trendsmap.com), this is a nice site for seeing trends on a map. Can be used to see whats happing around the world based off what people are saying on Twitter. Seems like a cool idea and I can see some marketing usefulness around it.

The Twitter API is REST based that returns JSON data back, so any languages that are able to make REST calls and decode JSON data should be able to use the Twitter API but I wanted to cheat abit and use a Ruby Gem to make my life easier.  I choose to go with the [Twitter gem by John Nunemaker](http://twitter.rubyforge.org/). As it seems to be the most used Twitter gem around... (also the first that showed up on Google). One thing to keep in mind when using the Twitter API is the number of calls you can make, 150 requests per hour and 350 OAuth'ed requests per hour. Because this is just me playing around with the API, I don't really care too much about how the Gem connects to the API and how many calls the API makes per Ruby call. If I was working on a app for work I can see myself writing out API calls myself or looking into the Gem to make sure there were no wasted API calls.

For the Geolocation part of the code I choose to go with [Geokit](http://geokit.rubyforge.org/) gem. This gem seems to be maintained and recently updated than the others I looked at. It uses both Google's and Yahoo's API for Geolocation which from my testing seem to return about the same info.

Based on your OS you should be able to run something like this to install the gems,
`gem install twitter geokit`
and here is the code.

{{< gist amscotti 5473624 >}}

Keep in mind this isn't getting Geo data from their posting, this is the info they have entered for their profile location and because of this it may not be truthful, right or even filled out. I would say the next steps would be to map out this data in some way in a Google Map. I may also write some code that would look at the Geo data from the postings themselves and map them out. Sadly a lot of people don't have Geo turned on when they are posting.

If you have any questions or comments please post, also any suggestions on improving this are welcome.
