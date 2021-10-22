---
title: "ClojureScript: Functional Programming for the Web"
date: 2021-10-22T14:01:45-04:00
draft: false
tags:
- Clojure
- Vermont
---

As I sit next to a gas store in Vermont, I once again have a hard copy book with me to read on vacation. This time it's "[Learning ClojureScript](https://www.learn-clojurescript.com/)" by [Andrew Meredith](https://twitter.com/a4w_m6h), and just like [Clojure For the Brave and True](/post/for-the-brave-and-true/) it's another free book that can easily be downloaded and read from any fancy gizmos. Unlike my trip to Italy, I have no fear of misplacing or having a piece of technology stolen because we are staying in one place for this trip. So I'll simply say I enjoy the feel of a hard copy book that I find better to read than a PDF or something on an e-reader. Being able to quickly flip back a page to re-read something or look ahead to see what is coming is something I don't think an e-reader will replace in the same way.

![Learning ClojureScript by a gas store in Vermont](/images/clojurescript-functional-programming-for-the-web/gas-store.png#c)

At this point on my vacation, I'm a little over halfway through the book, and I feel this has given an excellent introduction to Clojure(Script) and what actual development feels like. I have enjoyed using Clojure to create small command-line applications, do code katas, and create servers. But I haven't looked into what development looks like using ClojureScript, even though a lot of my desire to learn functional programming languages often comes from wanting to use them on the frontend.

After working in a legacy AngularJS for over three years, I feel that using a functional programming approach for frontend development helps tremendously with code complexity and readability. I would even argue there is more of a benefit for functional programming on the frontend than on the server due to the number of different states a UI can have and the complexity.

This is why languages like [ClojureScript](https://clojurescript.org/), [Elm](https://elm-lang.org/), [F# with Fable](https://fable.io/) and [ReScript](https://rescript-lang.org/) get me excited, as I feel they have huge benefits beyond just using a functional approach. Things like enforcing immutable data and leaning towards using more pure functions to build your application. Yes, you can do all this in JavaScript with some additional libraries and take care not to break the rules, but that takes time and effort away from you and your team where you can have a language that enforces a better way of writing software. As someone who has reviewed many pull requests, anything that software can do to help me review code is a win!

"Learning ClojureScript" echos a lot of ideas I covered in a [tech talk](https://github.com/amscotti/functional_programming_talk) that I gave at work on functional programming some weeks ago, and it reinforces the idea of using a functional programming language for writing frontend UI. In my talk, I pointed out a paper called [Out of the Tar Pit](http://curtclifton.net/papers/MoseleyMarks06a.pdf) by Ben Moseley and Peter Marks that goes over complexity in the development of large scale systems, and there is a lovely quote that sums up their findings of using functional programming,

> "Functional programming goes a long way towards avoiding the problems of state-derived complexity. This has very significant benefits for testing (avoiding what is normally one of testing's biggest weaknesses) as well as for reasoning."

As we work on a long-term project, we need to consider ideas that can help reduce complexity, help with state management, and create readable code that is easy to reason about. I feel that functional programming languages help with all this and bring back some of the enjoyment of development. I feel happy when using a functional programming language and will continue learning and sharing my experiences with others.

Until then, I will enjoy some hot cocoa and continue relaxing next to this stove in Vermont!