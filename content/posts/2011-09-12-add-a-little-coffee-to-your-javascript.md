---
author: Anthony Scotti
date: 2011-09-12T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- CoffeeScript
- Howto
- Javascript
title: Add a little coffee to your Javascript
url: /2011/09/12/add-a-little-coffee-to-your-javascript/
---

So for my posting for [Project Euler 001]({{< relref "2011-09-05-project-euler-001.md" >}}), the Javascript code kind of upset me. It's not nice to look at and doesn't really solve the problem in a functional way. With Javascript being a functional programming language it didn't sit well with me.

Comparing the Javascript code to the Groovy and Ruby code there is one thing missing and it is the 'Range' type call. If I could have a call like that I could use some other calls like filter and reduce to get the same outcome. Well, really this is a function that I need to add myself.

```
range = function(n) {
  _results = [];
  for (_i = 0; _i <= n; _i++){ _results.push(_i); }
  return _results;
}
```

This function should output an array, which will have calls for filter and reduce.

```
console.log(range(999).filter(function(n) {
    return (n % 3 == 0 || n % 5 == 0)
}).reduce(function(a, b) {
    return a + b
}))
```

I feel a lot better about this code. I made a function that I can re-use at any time and I use built-in function calls. I have updated the gist with the new code, [http://bit.ly/iNH5Pm](http://bit.ly/iNH5Pm).

What really got me thinking about this was some talks at NFJS Boston 2011, (which I hope to do a other posting about soon). Functional programming seems like something that a lot of people are talking about and a topic I plan on following more. After listening to some talks from [Venkat Subramaniam](http://twitter.com/venkat_s) on Javascript and Scala, and listening to a talk on [CoffeeScript](http://en.wikipedia.org/wiki/CoffeeScript) it's got me thinking more about how to use Javascript to solve problems.

Ah, CoffeeScript! This is where I got the idea of the range function. For the people that don't know what CoffeeScript is, it's a pre-compiled code that gets turned into Javascript. Think of Python/Ruby code that gets turn in to useable Javascript. Type less and do more. Think of it more like [Haml](http://haml-lang.com/) or [Sass](http://sass-lang.com/) code that is turned into HTML/CSS.

From my understanding, the project was first made for self use by 'Jeremy Ashkenas', but quickly caught on and is being used in some big places, I would say the biggest is in Rails 3.1. CoffeeScript has also been added to CouchDB for making views.

What's this code look like in CoffeeScript?

```
console.log ([0...1000].filter (n) -> n%3 == 0 || n%5 == 0).reduce (a,b) -> a+b
```

The \[0...1000\] part gets turned into a function like the one above. Here is the full Javascript output:

```
var _i, _results;
console.log(((function() {
  _results = [];
  for (_i = 0; _i < 1000; _i++){ _results.push(_i); }
  return _results;
}).apply(this).filter(function(n) {
  return n % 3 === 0 || n % 5 === 0;
})).reduce(function(a, b) {
  return a + b;
}));
```

Cool, right? I feel I am drawn to CoffeeScript because I have a background in Python & Ruby which the syntax was inspired by. CoffeeScript can also be used to help learn Javascript as you can see how complex code gets converted. I am going to be playing around with CoffeeScript here and there. I may even try to use it at work to help speed up some Javascript development.

As always, if there is a way to make this better or you have some great resources for learning/using CoffeeScript please share!
