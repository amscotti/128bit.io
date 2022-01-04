---
author: Anthony Scotti
date: 2014-08-31T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- RPC
- Redis
- Ruby
- Python
title: RPC using Redis
url: /2014/08/31/RPC-using-Redis/
---

One of the things I find myself always looking into and being excited about is scaling out systems. Now this means different things to different people.  The reason for me looking into RPC is how to deal with [Microservices](http://martinfowler.com/articles/microservices.html) as part of a way to move Monolithic applications to into the Microservices architecture.

RPC [(or Remote procedure call)](http://en.wikipedia.org/wiki/Remote_procedure_call) is an idea that has been in computer science for a bit now. An over simplified way of thinking about is the ability to send a message to a remote process whether it is on the same system or remote. Overall this is very vague and is open to many implementations. In my mind, there are too many things in play when it comes to RPC, the format of the message and how you get the message to the remote process. There are many ways to do RPC and this is just my take on it but for this posting I am going to use '[JSON-RPC](http://en.wikipedia.org/wiki/JSON-RPC)' for the message formatting and Redis as the way of pushing messages around.

## RPC vs Message Queue
The ideas are mostly the the same but with RPC the client is waiting for a return message that has the results from the RPC call. If your Message Queue system allows you to address messages back to the sender then you can most likely use it for RPC. In most Message Queues, they are used to trigger jobs that are not needed to reply to the client.

## Why Redis and not something else?
You should be able to find Redis in most modern tech stacks somewhere, and if not, what's wrong with you? Redis is a great tool for many things and you should really look into it.  With the idea of the path of least resistance and not needing to learn anything new, Redis fits into this perfectly, so let's see what we can do.

## Code

### Client
{{< gist amscotti f03f3c9ebe78b28f7223 "client.rb" >}}

### Server
{{< gist amscotti f03f3c9ebe78b28f7223 "server.rb" >}}

So, this works due to Redis having commands to let you block as you wait for data to come back from the server.  This is really nice as the client code looks like you are calling a local method.

## Ruby to Ruby is cool, but...
What if you want to use some other language? Well, as long as your language has good Redis library you should be able to do the same thing. Let's take a look at setting up a server in Python.

{{< gist amscotti f03f3c9ebe78b28f7223 "server.py" >}}

## Conclusion
This is very much a proof of concept to test some ideas in my head,  definitely needs more work around handling exceptions. If you see any issues with this approach I would love you to reach out to me. I do hope to look into using [RabbitMQ](http://www.rabbitmq.com/) at some point for the same idea but this could be a great approach if you already have Redis in your stack.
