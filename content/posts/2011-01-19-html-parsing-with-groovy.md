---
author: Anthony Scotti
date: 2011-01-19T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Groovy
- Howto
- HTML
- NFL
- Parsing
title: HTML Parsing with Groovy
url: /2011/01/19/html-parsing-with-groovy/
---

In a perfect world all the websites we would go to would be well formatted to the point that we could call them XHML so we could parse the data just like any other XML file but sadly this is not true. There is a lot of errors on pages that your browser fixes in the background or just simply overlooks due to HTML being so lose in its formatting structure. Due to this, the approach of parsing HTML could be a tedious one, but Groovy helps you by letting you call in [TagSoup](http://home.ccil.org/~cowan/XML/tagsoup/) which helps deal with poorly formatted HTML and gives SAX interface that can be used with standard XML tools.

I found myself using this last night trying to parse data from nfl.com for a friend, needing to look at the info in a table and make some kind of usable data structure from it.  It turns out to be as easy as parsing a XML file with using TagSoup. Here is a part of the code I used to pull the data and should get you started if you ever find the need to parse some HTML.

{{< gist amscotti 5478493 >}}

The output of this isn't that great, this is just to show how you would grab some data from the HTML page using TagSoup along with the @Grab in Groovy. Later I will most likely be pushing this data into a database.... maybe a noSQL database! :)

If you have any questions or comments please post, also any suggestions on improving this are welcome.
