---
author: Anthony Scotti
date: 2011-11-21T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Howto
- Ruby
- Sinatra
title: Authentication with Sinatra
url: /2011/11/21/authentication-with-sinatra/
---

One of the things I'm heavily looking in to is [Sinatra](http://www.sinatrarb.com), it's a micro-web framework which I feel gives you more freedom over your project and lets you rapidly prototype things out. You are able to keep a full app in one file which is perfect for use with Github's Gist. Sinatra lets you quickly build web apps in a short amount of time with less complexity then a Rails app.  A lot of places that host Rails apps will also host Sinatra apps using Rack. A place where I plan on releasing one of my projects is [Heroku](http://www.heroku.com). They are willing to give you a free web node, for small apps this will do fine and if later on you need to scale up it's easy to do.

I couldn't find any clear way of doing authentication within a Sinatra app so I made up some code that I hope will give people an idea on how to start.

{{< gist amscotti 1384524 >}}

Again, the hash is used in place for a database just for the sample. You really want to replace this with some database back-end.

If you see anyway of making this code better please comment or fork the Gist
