---
author: Anthony Scotti
date: 2011-02-17T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Groovy
- MD5
- Python
- Ruby
- Tip
title: MD5 hashing in Python, Ruby and Groovy
url: /2011/02/17/md5-hashing-in-python-ruby-and-groovy/
---

Hopping around from languages to languages, its easy to forget how to do something, nothing that a quick Google search can't help with but I wanted to make this posting for myself to save some time. [MD5](http://en.wikipedia.org/wiki/MD5) is used all over the place, its a one way hash that can be used for checking the integrity of files, storing passwords in databases and checking text being passed around. I do want to add a note here about using MD5 hashes for storing passwords in a database, I would start by looking at [SHA-1](http://en.wikipedia.org/wiki/Sha1) along with using salt this will help ensure if anyone gets a hold of your database they can just use [rainbow table](http://en.wikipedia.org/wiki/Rainbow_table) to workout the plain text of the password.

## Python
{{< gist amscotti 2467512 "md5.py" >}}

## Ruby
{{< gist amscotti 2467512 "md5.rb" >}}

## Groovy
{{< gist amscotti 2467512 "md5.groovy" >}}

So as you see from the code there are 2 ways to get a hash, one is to quickly get the hash from the text and the other is to update the digest. You would want to use the update method when you are reading a lot of data, for example a file. This will let you read part of the data and add it to the digest part by part. If you just need to check some text you can easily do so with one command.

If you have any questions or comments please post, also any suggestions on improving this are welcome.
