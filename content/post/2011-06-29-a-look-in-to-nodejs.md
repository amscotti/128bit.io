---
author: Anthony Scotti
date: 2011-06-29T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- DotCloud
- Express
- Javascript
- nodeJS
- Opinion
- Socket.io
title: A look in to nodeJS
url: /2011/06/29/a-look-in-to-nodejs/
---

![NodeJS Logo](/images/logo/node_js_logo.jpg)

NodeJS is a new take on a way to build scalable network services. Note that I didn't say web applications as nodeJS can do far more then just web apps. I've heard of people making IRC chats servers and DNS servers. So the capabilities of nodeJS go beyond just making web apps, but for myself this is my primary interests in nodeJS, but more precisely being able to make real time web apps. Real time web apps seem to add a more richer user experience along with being able to optimize your app to be able to receive pushed information over pulling and dealing with small packets of information and not a full page reload.

The part that sticks out to people about nodeJS is being able to write a server using Javascript. Why Javascript? From my understanding there are two main ideas behind this, more software developers will at one point in their life be dealing with Javascript and a good section of the development community will have this as a common language in their skill-set. This makes the entry level to get in to nodeJS lower then say Ruby/Python. The other idea is that Javascript has no predetermined notions on how to deal with file IO, but means the creator of nodeJS, Ryan Lienhart Dahl made Javascript file IO work the way he thought would be best. Looking at how file IO is done within nodeJS and also looking at the other calls, there is a huge emphasis on non-blocking code that is event driven. Due to these ideas, nodeJS has the ability to become quite scalable For myself this is a new way to think of coding but after doing some small projects, I kind of like it.

As I said my primary focus is on making web apps, mostly real-time and I found this is easy to do with nodeJS along with some packages. Ah, packages... if you are coming from the ruby world you know about gem, well there is something just like that for nodeJs, its called [npm](http://npmjs.org/) (node package manager) this will let you install some nice packages. You are able to install packages per project or system-wide based on how you want to use the package.

Here is a link to an example that I have made which is hosted on Heroku, [http://nodejsmapexample.herokuapp.com](http://nodejsmapexample.herokuapp.com/)

[![Screen Shot](/images/a-look-in-to-nodejs/Screen-shot-2011-06-28-at-10.58.15-AM-300x256.png)](/images/a-look-in-to-nodejs/Screen-shot-2011-06-28-at-10.58.15-AM.png)

What should happen if all goes well is the site using HTML5 API should ask for your geolocation, then it shows you where you are on the google map. After a bit anyone else looking at the page should appear on your map and their ID listed on the side. Very ruff right now but I wanted something that would show off nodeJS. To make this I used [Express](http://expressjs.com/) and [Socket.io](http://socket.io/). Express lets you build web apps in a [Sinatra](http://www.sinatrarb.com/) style. Express also comes with a template engine for HTML called [Jade](http://jade-lang.com/) which is heavily influenced by [Haml](http://haml-lang.com/). Now onto the real time pushing of new clients looking at the page, I used Socket.io. After getting new latitude and longitude coordinates, it gets sent to the server where it is then broadcasted to all people looking at the page. This code is on Github, [https://github.com/amscotti/nodejsmapexample](https://github.com/amscotti/nodejsmapexample). Anyone that is interested in updating the project I'll incorporate your updates and push them to the server and give you credit.

I'm still very much learning nodeJS and trying to up my Javascript skills, any comments or any way to improve this would be great!
