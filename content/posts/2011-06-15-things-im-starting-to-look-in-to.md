---
author: Anthony Scotti
date: 2011-06-15T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Continuous Integration
- CouchDB
- Crucible
- FishEye
- JenkinsCI
- MongoDB
- nodeJS
- noSQL
- Personal
title: Things I'm starting to look in to
url: /2011/06/15/things-im-starting-to-look-in-to/
---

Haven't blogged in some time so I wanted to give a quick update on the things I'm looking at for myself and work. Right now my group is coming to the end of a big project at work so a lot of my time has been going into that, but I've still been looking at some new things that I hope to later write postings about.

Right now the first item on the top of my list is [NodeJS](http://nodejs.org/), node is a way to build scaleable web applications by using just JavaScript. It uses the idea of non-blocking, and event driven code . By doing so you get a nice boost in performance but the part that I'm really looking at is using node to make real time web applications.

Next would be noSQL, I've been looking at this for sometime on and off. Mostly focusing at Document databases like [MongoDB](http://www.mongodb.org/) and [CouchDB](http://couchdb.apache.org/). RDBMS databases has been used for years and solved a lot of issues that people have had over time, but with the emersion of web applications we are seeing new problems were noSQL can solve. RDBMS is becoming a general purpose type of database where noSQL target precise problems that people are having.

Last but not least is [Continuous Integration](http://en.wikipedia.org/wiki/Continuous_integration), this is a topic mostly for work but something I want to learn to make myself a better developer. The main idea of CI is to help with quality control by pulling any updates from your revision control systems, building the your software and  then running all your tests. You should be notified right away if there is an issue at any point. This helps ensure your code is always passing the tests and if not you know about it right away to fix the issue. All this in hopes of getting one step closer to continuous deployment. The main tool I'm looking at for CI is [Jenkins](http://jenkins-ci.org/), free and open and easy to get up and running for testing with. Along with Continuous Integration, other tools that help with a development team, like [FishEye](http://www.atlassian.com/software/fisheye/) and [Crucible](http://www.atlassian.com/software/crucible/) from Atlassian. FishEye and Crucible both help with looking at your code base and doing code reviews and in turn help up the quality of your code. Atlassian makes great software, it makes looking at your code very easy and doing code reviews painless.

I'm hoping by next week I should have a posting on one of the topics here.
