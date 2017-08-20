---
author: Anthony Scotti
date: 2013-06-01T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Yeoman
- APIs
- NodeJS
title: Yeoman working with APIs
url: /2013/06/01/yeoman-working-with-apis/
---

From my [last post]({{< relref "2013-05-28-my-friend-yeoman.md" >}}), I talked about how great Yeoman is. I have found one issue with Yeoman but there is a easy solution. Yeoman comes with its own built-in server which is very convenient, but if you're working on a application which requires access to an API this becomes an issue due to cross site domain.

For some time I've been making a symbolic link of my Yeoman app folder into my Tomcat's webapp folder which would allow me to access the API running on the same server. Since I am both a back-end and front-end developer, having the set up is not too much of an issue for me. Thinking from a point of view as someone new working on just the front-end of this project, the setup needed is kind of a pain due to a requirement of having the full stack running on your local system.

My solution to this was to setup a local server that could proxy calls to the API. I made a small Node.js server that uses [Connect](http://www.senchalabs.org/connect/) and [http-proxy](https://github.com/nodejitsu/node-http-proxy).

Here is the code,

{{< gist amscotti 5236433 >}}

To setup the dependencies in your package.json file add in this,
```
   "http-proxy": "0.8.x",
   "connect": "2.3.x"
```
Then run `npm install` to install them.

If you want to take this one step farther, you can also add this to your package.json
```
 "scripts": {
    "start": "node server.js"
  }
```
This will add a command to npm that will let you now run `npm start` and it will load the server for you.

This cuts down the over head of what I need to run just to work on the front-end code and lets other developers on the team quickly work on the project too. I hope this helps anyone working with Yeoman on apps that need to talk to a API.
