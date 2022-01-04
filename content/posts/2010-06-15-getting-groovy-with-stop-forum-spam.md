---
author: Anthony Scotti
date: 2010-06-15T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Forums
- Groovy
- Howto
- Spam
- XML
title: Getting Groovy with Stop Forum Spam
url: /2010/06/15/getting-groovy-with-stop-forum-spam/
---

Spam sucks and administrating a forum that is phpbb3 based you find there are a lot of bots that sign up and try to post spam. It's a pain to go through by hand and remove them all due to some of them being really clever and looking like real people. This is where a great site like [stopforumspam.com](http://www.stopforumspam.com) comes in to play.  You are able to search users based on email, username and IP to check to see if they have been reported as a spammer before.

Stopforumspam also has a nice API that you are able to quickly access by passing email, username or IP and it will return XML letting you know if they have been reported before. I wanted to take some of thing I learn from my last groovy posting and write something new and using the stopforumspam's API seems like a great place to start. Sadly the the forums at [controlledchaos-guild.com](http://www.controlledchaos-guild.com/forums/) are hosted on Godaddy and they seem to block connects to the mySQL database... (I really need to move them off of Godaddy and onto the same server as this blog, but that's a other story) so I take all the user's email and dump them to a text file.

Here was the code that I came up with:

{{< gist amscotti e5aaacef6d738078c65201a94fe7cfb4 >}}

The output looks like this,

```
gdsfgdfsg@romantyczka.pl has been reported 52 times on stopforumspam.com
patrickzjunior@gmail.com has been reported 18 times on stopforumspam.com
16@scottsdaleazwindshieldrepair.com has been reported 17 times on stopforumspam.com
669@26up.com has been reported 154 times on stopforumspam.com
304@wep6.com has been reported 40 times on stopforumspam.com
profilemakers199@gmail.com has been reported 207 times on stopforumspam.com
```

About 5 lines of code to do this, not bad at all. Thinking to myself, I don't think I could do this with any other language using that few lines but I wouldn't mind someone showing me! The Groovy code is very readable. Usually I find a lot of code that people cut down lines become hard to read, this is not the case with Groovy.

For the people that want to work directly with their database take a look at [http://groovy.codehaus.org/Database+features](http://groovy.codehaus.org/Database+features) to get an idea of what you would need to do. It's really not going to add to much to your code!

I'm stilling trying to learn Groovy so if anyone knows a better way of doing this please share, also feedback and questions are welcome!
