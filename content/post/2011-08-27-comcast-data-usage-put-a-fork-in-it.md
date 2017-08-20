---
author: Anthony Scotti
date: 2011-08-27T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- GitHub
- Howto
- Mechanize
- Nokogiri
- Ruby
- Screen Scraping
title: Comcast data usage, put a fork in it!
url: /2011/08/27/comcast-data-usage-put-a-fork-in-it/
---

Yesterday I was looking around for some new Ruby gems to help with [web scraping](http://en.wikipedia.org/wiki/Web_scraping) (also sometimes called screen scraping), I found [Nokogiri](http://nokogiri.org/) which is a great gem for dealing with HTML/XML data. One of the great things about Nokogiri is that it lets you use CSS3 selectors to find the data your looking for. This kind of makes it like using jQuery but in Ruby. For working with one page and not interacting with a site Nokogiri is fine, but if you need something more, [Mechanize](http://mechanize.rubyforge.org/) most likely will do the trick. The Mechanize gem lets you interact with the site but uses Nokogiri to find the data on the site. You are able to fill out forums for logging in and clicking links and so on. Your also able to tell Mechanize what user_agent to look like.

So with my new found powers I wanted something to test with, after thinking for a bit I came up with trying to pull the Comcast data usage from the user page. If you are not a Comcast user you may not know that Comcast limits you to only using 250GB per month, you are able to go over but they don't really like it and bad things can happen to you. To have something that can report to me how close I'm getting to my cap would be nice. Thinking this maybe a common problem, I started Googling to see if anyone else had something. I [found this posting](http://wonko.com/post/ruby-script-to-display-comcast-data-usage) made back in 2/2010 which from reading the comments and testing the code had stop working due to Comcast updating their site, which happens a lot to older web scrapers. Luckily [rgrove](https://gist.github.com/rgrove) posted his code to github's gist letting me easily fork the code giving me a good starting point to work with.

Here is the code I come up with,

{{< gist amscotti 1174897 >}}

Run it from the command line like so
```
$ ./capmon.rb <username> <password>
```
and it should output something like this,

![Screen Shot](/images/comcast-data-usage-put-a-fork-in-it/Screen-Shot-2011-08-26-at-11.03.38-PM.png)

So as of this posting, this code is working and should give people a good starting point to add on to for reporting or alerting you if you get to close to your 250GB cap.

Some helpful links for learning about both Mechanize and Nokogiri,

*  [Railscast's #190 Screen Scraping with Nokogiri](http://railscasts.com/episodes/190-screen-scraping-with-nokogiri)
*  [Railscast's #191 Mechanize](http://railscasts.com/episodes/191-mechanize)

Open for questions, comments, or any way to improve this!
