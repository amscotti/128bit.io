---
author: Anthony Scotti
date: 2012-06-02T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Heroku
- nodeJS
- Personal
- Ruby
title: Small updates
url: /2012/06/02/small-updates/
---

Nothing too big but I did some small updates to two of my projects; amscotti.com and Nodejs map example.

### Node.js Geolocation Map Example

This is a project that I did awhile ago when learning node.js. Because things are new in the node.js world, the libraries update often and the ones I used (Mostly Socket.io) did change and needed some updates to get it working again with the newer versions. I also wanted to move the hosting from [dotCloud](https://www.dotcloud.com) to [Heroku](http://www.heroku.com), the new address is at [http://nodejsmapexample.herokuapp.com/](http://nodejsmapexample.herokuapp.com/). Nothing wrong with docCloud, I just have other apps on Heroku and I like using the Git workflow to deploy my apps better then docCloud's approach. I did have to make one change when moving to Heroku with socket.io and that was to force the transport to use xhr-polling, which is [required](https://devcenter.heroku.com/articles/using-socket-io-with-node-js-on-heroku) to use socket.io on Heroku.

### amscotti.com

As always this is a work in progress and I still need to do some more work to it but I wanted to do some quick update for performance. First, I added settings for production mode to be able to use assets off of CloudFront, a [content delivery network](http://en.wikipedia.org/wiki/Content_delivery_network) service from Amazon, that lets you push files from a S3 bucket to the CDN. The hope of this was to take some load off the server and because it's on a CDN it should always use a server closest to the user. The next thing I did was to switch from Thin to [Unicorn](http://unicorn.bogomips.org/) for a bit of a boost in performance. Unicorn allows you to have additional processes for serving your application. By using the [blitz.io](http://blitz.io/) add-on from Heroku I am seeing some good improvements with the changes I have made. Still many updates need to be made to the site but for now I'm happy with the performance boost.

The code for both projects are on GitHub, feel free to take a look and suggest any improvements you see. I would love to know if I can improve anything else!
