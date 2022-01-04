---
author: Anthony Scotti
date: 2013-04-27T00:00:00Z
email: anthony.m.scotti@gmail.com
title: New Post with a new site layout!
url: /2013/04/27/new-post-with-a-new-site-layout/
---

Well, if you remember my old site then you know that this is a big change from what I had before. I have fully redone the blog moving it from my old hosting to Amazon S3 using static files with the help of [Jekyll](http://jekyllrb.com/).

## Why?

I was using Wordpress before, which is great blogging software but a bit over powered for the way I was using it. It's was written in PHP using a MySQL server to build dynamic pages. For my blog I don't need the overhead of a server to build dynamic pages. The site is very static and I can rely upon JavaScript for anything that I need to be dynamic.

## Hosting?

Because I'm using static files I'm able to host the site just about anywhere, I've heard people using GitHub or Dropbox to host their blog. I chose to use [Amazon's S3](http://aws.amazon.com/s3/) because it's very easy, very fast, and links with Amazon's CloudFront so my content will be spread across the CDN network.

## Layout?

My original blog I wanted a nice clean layout, which for the most part it was but I was always limited by the templates that Wordpress used. I was not interested in learning how WordPress templates are made or how to edit them.

Jekyll uses standard HTML and CSS for its layout, which is the standard way of laying things out all across the web. Twitter Bootstrap was used for the layout, this works well across browsers and on mobile.

I'm far from a web designer but I think the postings are very clean and easy to read which is what I was aiming for. There are some small issues on mobile when reading code that has been posted to GitHub.

## Blogging?

The frustrations I had with WordPress was the editor didn't quite do exactly what I wanted to do. Also you could only write your postings from the web interface, which if you were offline was useless.

Right now I'm typing this blog into a text editor, it happens to be [iA Writer](http://www.iawriter.com/mac/) but it could any [TextMate](http://macromates.com/), [Sublime](http://www.sublimetext.com/), or even Vim. I've the freedom to type this anywhere!

Jekyll uses markdown formatted text for its blog posting, it is the same formatted text that you find on [GitHub](https://github.com/) or [Trello](https://trello.com/) and many other places online. Is pretty standard and very easy to learn and nice to look at in my opinion.

Another thing I really enjoy is an actual preview of what the posting will look like. Running a local server that will regenerate the files every time I save. I just need to keep the posting open in the browser and refresh to see my updates.

## What is missing?

So even though the new site is up there's a lot that is missing. I consider this very much a work in progress. I feel that if I keep working on it, it would never be released anytime soon. I very much want to get back into blogging but still want to maintain some my more popular postings.

* Currently there are no comments on site (not that anyone really used them)
* Tags are still in the postings but templates are not using them
* There's no archiver or any easy way to search for a posting
* The design is still a bit raw in some areas

## Anything else?

With the new design I'm now considering taking on guest postings. Depending on what I come up with, the guest would supply me with a posting and optionally a template if they chose to have a different format than the one I have on the site right now. Full credit would be given to the guests along with links to their blogs.

I'm going to be setting up a GitHub repository for the blog that will contain all the postings. This will provide a way for people to comment on any postings or even make their own edits by submitting a Pull Request.
