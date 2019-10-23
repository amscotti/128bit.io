---
title: "For the Brave and True"
date: 2019-10-23T22:43:11+02:00
tags:
- Books
- Clojure
- Development
- Italy
---

In my last post, I said I was in Italy on vacation and you may be thinking to yourself (most likely not, but just go with it) "what high tech gizmos did he bring with him on his travels?" and I would happily reply "A book!", yes a paper book. Being a software developer, I have access to tons of technology, more so when it comes to paper book replacements but there is just something about a real book that makes reading and learning for me better than using a computer, tablet, or doohickey. 

Another really great advantage of a paper book is if you happen to lose a book when traveling its much less money to replace than a fancy gizmo. Also, I’m guessing that most people will not be interested in stealing a book on the next hot programming language, but you never know.

{{< instagram B3-ZWAvnD1U hidecaption >}}

So, all this is a long about way to talk about the book I’m reading right now which is "[Clojure For the Brave and True](https://www.braveclojure.com/clojure-for-the-brave-and-true/)" by [Daniel Higginbotham](https://twitter.com/nonrecursive). Why Clojure? Being a functional programming language, I always had it in the back of my mind as something to learn but sadly never on the top of the list. After hearing a good number of people talking about Clojure I figured I would boost it up the list and give it a look and I'm happy I did! They're tons of good reasons to learn Clojure, I'll talk about some interesting points I have found so far.

Clojure being a dialect of [Lisp](https://en.wikipedia.org/wiki/Lisp_(programming_language)) always seemed very foreign to me coming from languages like Java, Ruby, and Python but after playing around with it for a bit, the unique syntax does start making sense. An interesting thing about Lisp dialects is that they are very similar, and the language doesn't change much over time. Someone that wrote Lisp in the 60s would be able to understand a new dialect like Clojure. Comparing Clojure's syntax to something like JavaScript's which has changed from year to year makes Clojure very much a relief and a testament to how much time and research has gone into Lisp. 

Besides the unique syntax, Clojure has immutable data structures that are useful for anyone that has worked on a large application before and found it hard to understand the flow of data. Immutable data structures typically forces an application structure that creates easy to understand flow by using pure functions that take inputs and return outputs. Because pure functions are easier to reason about and to test, we are starting to see similar ideas appear in other languages along with libraries for languages without immutable data structures.

Clojure also has something that I have only played within Haskell before, lazy evaluation. This is a very interesting concept where you can hold off on evaluating a value until the point it's needed, so if you have something that takes a significant amount of computational time you will only pay the cost when you use that value in your code. This also lets you create sequences of infinite length but only use what you need, this is something that really fascinates me because you really start thinking about solving problems in different ways. 

Clojure embraces a lot of the ideas found in other functional programming languages but it is also more of a pragmatic language which makes it easier to do real work and get things done quickly. To contrast this, I enjoyed learning Haskell but I couldn't get past solving small exercises on [Exercism](https://exercism.io/) due to its pureness, but with Clojure, I have already been able to build some small real-world apps. (Haskell is a great language but does focus on different values then Clojure)

There is so much more to Clojure than I could go over in one post, with the fact that I'm also still learning Clojure myself, but I do want to point out one more thing that really excites me, [ClojureScript](https://clojurescript.org/). Being able to take all the great things from Clojure and target JavaScript to write web applications. For me, this makes learning Clojure even more useful with the idea of being able to replace JavaScript with a functional programming language like Clojure.

So, Clojure is great but how is the book? (As you ask in this theoretical conversation) The book is great, I would say it's one of the greatest programming language books I have read in some time. There is a good mix of humor along with step by step learning of Clojure along with functional programming. So far, every chapter has a fairly good size program that you create as you read through the chapters, along with exercises to do on your own. Overall reading Clojure For the Brave and True has been very enjoyable, and I would recommend this book to anyone that wants to learn Clojure but also anyone that would like to know more about functional programming.

## References
- [Brave Clojure](https://www.braveclojure.com/)
- [Clojure Data Structures](https://clojure.org/reference/data_structures)
- [Laziness in Clojure](http://clojure-doc.org/articles/language/laziness.html)