---
author: Anthony Scotti
date: 2014-09-07T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- MessagePack
- RPC
title: MessagePack
url: /2014/09/07/MessagePack/
---

One of the things I forgot to talk about in my [last posting]({{< relref "2014-08-31-RPC-using-Redis.md" >}}) was the use of MessagePack. MessagePack is a library that lets you take objects and convert them into something much smaller than JSON. Some people have reported using MessagePack and have saved up to 50% of space over JSON. That's not a bad saving for just using a library. In my example, I wasn't dealing with any objects that was too complex but there is still a benefit of using MessagePack.

This can make a big impact in many different places of your architecture when you have many systems talking to each other. MessagePack will cut down on the amount of data that needs to be passed around, along with how much storage is being used to save it. In my [last posting]({{< relref "2014-08-31-RPC-using-Redis.md" >}}) example, this helps out in both areas because we are transferring the messages into Redis to be stored until they are pulled (or until they expire). So, if you have a sudden spike in requests, you know that the messages are taking up less space in your database. Less space and faster transfer, seems like an overall win to me.

Give it a try and see if it fits your needs. In most cases it's as simple as making one or two lines of change to your code. You can find a MessagePack library for just about any language, I would be shocked if they didn't have them for your language of choice.

## Resources

* [MessagePack Home Page](http://msgpack.org)
* [MsgPack vs. JSON: Cut your client-server exchange traffic by 50% with one line of code](http://indiegamr.com/cut-your-data-exchange-traffic-by-up-to-50-with-one-line-of-code-msgpack-vs-json/)
* [My thoughts on MessagePack](https://gist.github.com/frsyuki/2908191)
