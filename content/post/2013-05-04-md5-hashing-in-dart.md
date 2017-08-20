---
author: Anthony Scotti
date: 2013-05-04T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Dart
title: MD5 hashing in Dart
url: /2013/05/04/md5-hashing-in-dart/
---

Here is some Dart code for doing MD5, though at this point in time, MD5 is becoming obsolete in favor of SHA1. But as I have done code for MD5 in other languages I figured I would duplicate the code for another comparison. To look at the languages, checkout [MD5 hashing in Python, Ruby and Groovy]({{< relref "2011-02-17-md5-hashing-in-python-ruby-and-groovy.md" >}}) and [MD5 hashing in CoffeeScript, Perl and Scala]({{< relref "2012-04-22-md5-hashing-in-coffeescript-perl-and-scala.md" >}}).

{{< gist amscotti 2467512 "md5.dart" >}}

I do like how you can use [Method Cascades](http://tmblr.co/Zl1k2ujH3EsC), this is something that I really wish Java had in it because the code is much cleaner in my opinion.

I am hoping to have some time to play around with Dart's Isolates. It is like a cross between JavaScript's [Web Worker](http://www.html5rocks.com/en/tutorials/workers/basics/) and [Erlang or Scala actors](http://savanne.be/articles/concurrency-in-erlang-scala/).

Got a way to make the code better? Fork the Gist or comment on Github.