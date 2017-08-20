---
author: Anthony Scotti
date: 2012-06-16T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- BrowserID
- Howto
- Mozilla
- Opinion
- Ruby
- Sinatra
title: Mozilla's BrowserID
url: /2012/06/16/mozillas-browserid/
---

If you look around the news you will always hear about some big name that has been hacked and had their password database compromised. In recent news, this has happened to many people like [these guys](http://blog.linkedin.com/2012/06/06/linkedin-member-passwords-compromised) and [them](http://blog.last.fm/2012/06/08/an-update-on-lastfm-password-security), but if you keep looking you'll find tons more. The topic of security and how you are storing passwords always comes up, but this is not the point of this posting. I wanted to take this time to point out a Mozilla based project which helps in this area. [BrowserID](http://browserid.org) is "A better way to sign in" that take use of Mozilla's service for storing the user's passwords and lets your application validate the user and log them in.

There are other services like this out there that achieve the same thing, but I feel that BrowserID is easy to setup and the overall flow seems very nice to me. In the end as a Developer I don't want to be dealing with boring user registration code and passwords validation when I can be writing my application and having fun working on new features. Also, not having that feeling at night right before falling asleep thinking about if your users passwords are safe or not is always nice too! ;)

I coded up a small example about how to use BrowserID with Sinatra. [All code can be found on GitHub](https://github.com/amscotti/Sinatra-BrowserID).

This is the haml index file,

{{< gist amscotti 5401306 "index.haml" >}}

This is the Javascript code which pushed the assertion code to the application's backend,

{{< gist amscotti 5401306 "app.js" >}}

This is Sinatra application code.

{{< gist amscotti 5401306 "app.rb" >}}

The overall idea is being able to check the assertion code you get back from the BrowserID server using the Javascript from your front end. This is done by just making a POST request to the BrowserID server with the assertion code. You should get JSON data back telling you if the user is validated or not. Based on this, you can do whatever you need on the backend to log the user in. There are some more options for [Persistent Login](https://developer.mozilla.org/en/BrowserID/Persistent_Login) that lets the user stay logged in to your site based on their signed certificate expiration time. This just gives you more options for managing the user's login.

If you are wondering if any site are using BrowserID, you will find that Mozilla has switched over to using it ([Eating your own dog food](http://en.wikipedia.org/wiki/Eating_your_own_dog_food)) along with [OpenPhoto](http://current.openphoto.me/). Also the Drupal community was able to make a [module for using BrowserID](https://www.acquia.com/blog/browserid-announcement-drupal-module-under-24-hours).

I have an open pull request for the [BrowserID Cookbook Repo on Github](https://github.com/mozilla/browserid-cookbook), so I'm hoping the code will be added soon.

Here are some resources links,

*  [BrowserID Developer Page](https://developer.mozilla.org/en/BrowserID)
*  [Protocol overview](https://developer.mozilla.org/en/BrowserID/Protocol_Overview)
*  [BrowserID: Will it Succeed Where OpenID Failed?](http://dickhardt.org/2011/07/browserid/)

Any feed back is welcome, feel free to comment or fork the code on [Github](https://github.com/amscotti/Sinatra-BrowserID)!
