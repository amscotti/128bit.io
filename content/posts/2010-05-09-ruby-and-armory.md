---
author: Anthony Scotti
date: 2010-05-09T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Howto
- Ruby
- Wow
- XML
title: Pulling data from the Warcraft Armory with Ruby
url: /2010/05/09/ruby-and-armory/
---


**Update:** New code using Battle.net's REST API can be found [here]({{< relref "2011-09-22-updated-world-of-warcraft-armory-code.md" >}}).


For the people that play World of Warcraft, you know there is a great site made by Blizzard that keeps all your characters and guild information called the armory. If you take a good look at the site you will see its XML being formatted by XSLT. This is really great for people that want to script something to pull data from the armory because XML is really easy to parse.

The idea of this code is to form the URL path and pull the XML to parse out the data we want. This code is just going to pull level 80s (max level at time of writing this) from a guilds list. You can take this further and start pulling data per character from that list but this is just to get you started. I am using Ruby because I'm trying to learn the ins and outs of it, but the same can be done in Python or any other languages that can handle downloading and parsing XML.

{{< gist amscotti ece62f9c9c1331b01e108a8eae94bd41 >}}

This will out put a nice list of all the level 80 toons and their class that are within the guild.
I'm sure there is a better way to do this and I would love to know, so if you know please leave a comment. Feedback is welcome as well!
