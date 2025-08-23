Title: Dart with a side of Popcorn.js
Date: 2013-05-19 00:00
Slug: 2013/05/19/dart-with-a-side-of-popcorn
Save_as: 2013/05/19/dart-with-a-side-of-popcorn/index.html
URL: 2013/05/19/dart-with-a-side-of-popcorn/
Tags: Dart, Popcorn.js
Summary: Demonstrates using Popcorn.js media library from Dart, solving JavaScript callback context issues. Shows working with Web UI package for HTML elements, notes Popcorn.js is no longer maintained, and explores Dart VM's positioning with web apps, questioning browser vendor support strategies.

**Update:** Popcorn.js is no longer maintained I have removed by Mozilla

So personally, I'm not interested in using Dart for building web applications, I'm more interested in the Dart VM but after watching [Vijay Menon's video on JavaScript Interop](http://www.youtube.com/watch?v=QFuCFUd2Zsw). I was interested to see how well Dart would work with a JavaScript library that I have been working with for a bit now, [Popcorn.js](http://popcornjs.org/).

Popcorn.js is a JavaScript library that is used for working with media, it will allow you to embed video and setup time-based interactions. There are [many good demos](http://popcornjs.org/demos) on the Popcorn.js site and it is worth taking a look.

![Dart and Popcorn](/images/dart-with-a-side-of-popcorn/dart_and_popcorn.png)

Code can be found on GitHub, [here](https://github.com/amscotti/dart_popcorn_demo).

I put together a small demo of using Popcorn.js from Dart, it's pretty straightforward, but works really well. This was also my first time for playing around with [Web UI Package](http://www.dartlang.org/articles/web-ui/). It seems very useful but coming from a JavaScript library like Backbone.js, Ember.js, and AngularJS, I find the structure a bit lacking but that could just be my lack of knowledge with Web UI.

Overall this seems like a great way to use the JavaScript libraries that you use or still need to use when building your web applications. As Vijay Menon says towards the end of the video, you do have to watch your memory usage but there is a way around that within the JavaScript interop library.

I'm curious how someone would access 'this' for a callback. Many times within a JavaScript callback you use 'this' but I couldn't find a way to access 'this'. I can see many reasons for not letting Dart access 'this' as it's a very difficult thing to understand and usually throws people off when writing JavaScript code and leads to many bugs.

Listening to Google I/O it seems that Dart will be presented to a standardization board after which efforts will be made to embed the Dart VM into Chrome. At this point I'm very interested in what other browser makers will think of Dart and if they will follow suit. Overall, I just hope that this does not create strife within the web community. Right now we all back a single language which allows us to focus more on tools and libraries to help us develop web applications with the introduction of Dart this could change the focus of many people, thus weakening many projects.
