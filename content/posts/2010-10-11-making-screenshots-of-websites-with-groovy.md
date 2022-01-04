---
author: Anthony Scotti
date: 2010-10-11T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Groovy
- Howto
- Java
- JTidy
- Renderer
- XHTML
- XML
title: Making screenshots of websites with Groovy
url: /2010/10/11/making-screenshots-of-websites-with-groovy/
---

For a project I needed to work out a way to make thumbnails/screenshots of HTML files for some Java code I was working on. From my research, I found a nice project called the [The Flying Saucer Project](https://xhtmlrenderer.dev.java.net/) which has an XML/XHTML/CSS 2.1 renderer which works for what I needed for my project. Taking the HTML files and using [JTidy](http://jtidy.sourceforge.net/) to make them in to XHTML the renderer could output an image file for me. You are also able to use the renderer to make PDFs and SVG files. I wanted to take the small part of my code that was written in Java and port it over to Groovy. As I'm still learning Groovy I'm sure there is way to make this code better and I would love some feedback!

Here is the code,

{{< gist amscotti 5473860 >}}

Here is the output from the code,

**www.128bitstudios.com**

![www.128bitstudios.com](/images/making-screenshots-of-websites-with-groovy/www.128bitstudios.com_-300x187.png)

**en.wikipedia.org**

![en.wikipedia.org](/images/making-screenshots-of-websites-with-groovy/en.wikipedia.org_-300x187.png)

**misplaced-packets.net**

![misplaced-packets.net](/images/making-screenshots-of-websites-with-groovy/misplaced-packets.net_-300x187.png)

**stackoverflow.com**

![stackoverflow.com](/images/making-screenshots-of-websites-with-groovy/stackoverflow.com_-300x187.png)

As you can see the output isn't perfect but if you are just making thumbnails it should be ok. It has issues when it comes to java script which on some sites are used for layout. If you have a site/HTML file that just uses HTML and CSS the output should be good. I would love someone that is better acquainted with Groovy to over look this for way to make the code more 'groovify'.

Open for questions, comments, or any way to improve this!
