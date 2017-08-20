---
author: Anthony Scotti
date: 2013-05-02T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Dart
title: Using Dart with Blizzard's Battle.net API
url: /2013/05/02/using-dart-with-blizzards-battlenet-api/
---

As with a lot of postings on this blog, when I look into learning a new language I copy something I have done before. I have decided to use the Battle.net API to pull World of Warcraft data. It's an easy subject to reason about and show off parts of the language's syntax.

Also, as I have the same code in Ruby, Groovy, and CoffeeScript it's a nice comparison. You can find the other code as part of the [Updated World of Warcraft Armory code]({{< relref "2011-09-22-updated-world-of-warcraft-armory-code.md" >}}) posting.

{{< gist amscotti 1236553 "wowapi.dart" >}}

You will need to install the '[http](http://pub.dartlang.org/packages/http)' package from Pub to run this.

The 'as JSON' isn't needed to use the JSON parse method, but I feel that it's cleaner because 'parse' could be used for many things.

I like the syntax for setting up the map, but using it you can only have your keys be Strings. If you want anything else, you would need to add the items one at a time. It was easier for me to use toString on the int and keep the map in the nice syntax.

I couldn't find a way to have the map include a default key, but as long as we don't try to ask for anything that isn't in the map it will be fine.

The SDK comes with it's own JSON parser but I do like what [Chris Buckett](https://twitter.com/chrisbuckett) is doing with [JsonObject](http://pub.dartlang.org/packages/json_object). The syntax is nice and very familiar to JavaScript/CoffeeScript.

A great Dart resource is the [Dart Screencasts](http://dartcasts.com/).

Got a way to make the code better? Fork the Gist or comment on Github.

**Edit**: [Vyacheslav Egorov](https://twitter.com/mraleph/status/330267857722171392) on Twitter has pointed out to me that you don't need to create a closure if you are doing something simple, like parsing the JSON.
