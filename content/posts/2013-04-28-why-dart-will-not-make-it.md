Title: Why Dart Will Not Make It...
Date: 2013-04-28 00:00
Slug: 2013/04/28/why-dart-will-not-make-it
Save_as: 2013/04/28/why-dart-will-not-make-it/index.html
URL: 2013/04/28/why-dart-will-not-make-it/
Tags: Dart
Summary: A critical analysis of Google's Dart language strategy. Questions focus on web applications when most developers need backend work, wonders why Dart VM competes with V8 instead of improving it, and notes JavaScript's dominance despite Dart's quality. Suggests Dart team should better support backend development or explain performance positioning.

Yes, the title is a bit of a troll. I like Dart, I think it's a great new language made for the web! But, I do have some issues with the focus they have.

So one day a group of developers got together and declared that JavaScript is hard. It's hard to write good JavaScript code, it's hard to optimize it, and it's easy to write crappy code. I do not disagree with this but I feel you can write crappy code in any language, trust me I've seen it done. (Not in my code of course!)

How some people solve this problem is to use languages that compile into JavaScript for example [CoffeeScript](http://coffeescript.org/) (from [Jeremy Ashkenas](https://twitter.com/jashkenas)) or [TypeScript](http://www.typescriptlang.org/) (from Microsoft). These two solutions are geared towards two different set of people, CoffeeScript has a more familiar syntax to Ruby or Python developers where TypeScript is more geared towards C# or Java developers. I think both are great solutions because in the end you're just writing JavaScript.

Now here comes Google with its own brand-new language, [Dart](http://www.dartlang.org/). Unlike the other solutions mentioned above, Dart comes with it's own VM. Google is trying to make the language very familiar for Java or C# developers. Dart also gives you the ability to not only to write front end applications but also back-end applications.

Google is working to improve the Dart VM, making it as fast as possible. You can check out benchmarks from every commit [here](http://www.dartlang.org/performance/). Some of the people that are working on the Dart VM are the same people who worked on the V8, the JavaScript engine that is in Chrome. So I'm sure that they know how to make a high-performance VM.

I think this is all very great, and I'm very interested in anything that is high-performance, which is one of the things that attracted to me to NodeJS. Unfortunately the focus of the project only seems to be on building web applications in the front end. Dart does give developers a way to organize their code which is more optimized than using JavaScript. Still, no matter how much people would want the Dart VM in all major browsers it's not going to happen anytime soon. Which means you're still going have to compile your code into JavaScript to make use of it.

So why work so hard at making the Dart VM so optimized? Why even have the Dart VM if most people are building web applications and not back-end services? Why work on a language that is just going to compete with another language that your company is already working on, [Go](http://golang.org/)? Go is at least supported by Google App Engine.

I'm not opposed to having Dart VM in the browsers, but I would love the Dart team to give a bit more support for using Dart on the back-end. It's hard to find any good source of information for using Dart in this way. Most of the results that you find are about building web applications. 

If the back-end turns out not to be a focus of Dart that's fine with me, but then shut up about how fast your VM is compared to V8 because no one's going to be using it! If this turns out to be the case, it would have made more sense to improve V8 then the Dart VM.

Until the Dart team comes out and says the back-end is not the focus for them, I'll give Dart a chance. The language interests me even though the syntax looks like Java. I also feel they have an excellent team working on the VM that will keep improving over time. I would just like to take advantage of these improvements, if not in the browser, then on the back-end.

Good resources for Dart,

* [Dart in the Shell Video](http://www.youtube.com/playlist?annotation_id=annotation_226570&feature=iv&list=PL1id3ien5Lz-IBQP4ghxPbFbXGM8hd2UT&src_vid=Rh_kaQUXXX4)
* [Dart Tips](http://www.youtube.com/playlist?list=PLndbWGuLoHeaPgfKYlwJvDDxCrRdDbga3)
* [Dartisans - Dart Developers Live](https://www.youtube.com/playlist?list=PLOU2XLYxmsIIS2zgjdmBEwTrA6m5YgHBs)
* [Dart's plan to make it easier for you to build web apps](https://www.youtube.com/watch?v=9RCuW6K1afs)
* [Running Dart in the Cloud with Heroku](http://blog.sethladd.com/2012/08/running-dart-in-cloud-with-heroku.html)