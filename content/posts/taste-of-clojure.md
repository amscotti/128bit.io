---
title: "Taste of Clojure"
date: 2020-02-06T20:39:52-05:00
draft: false
tags:
- Clojure
- Development
---

Clojure seems to be coming up a lot in postings, books, and social media. Some most notable mentions are by [Gene Kim](https://twitter.com/RealGeneKim) in a couple of different instances, [Love Letter To Clojure](https://itrevolution.com/love-letter-to-clojure-part-1/) being the biggest but also in his book  [The Unicorn Project](https://itrevolution.com/the-unicorn-project/) where Clojure is a beloved language by Maxine the main ~~protagonist~~ hero of the story. Another well-known name that has talked about Clojure on his blog is [Robert Martin](https://twitter.com/unclebobmartin) (aka Uncle Bob) with his posting [Why Clojure?](https://blog.cleancoder.com/uncle-bob/2019/08/22/WhyClojure.html) and [Robin Schroer](https://sulami.github.io/) response to Uncle Bob's posting with [Why I like Clojure](https://sulami.github.io/posts/why-i-like-clojure/). One more link I want to share because I think this is one of the most beautiful introductions to Clojure I have seen [a smol comic about clojure](https://daiyi.co/blog/2017/07/19/a-smol-comic-about-clojure/) by [Daiyi](https://twitter.com/daiyitastic).

I think with all the links I have mentioned you should have a good sense of why you would want to learn Clojure and many of its great benefits. I don't think I would be able to give a better introduction and go into "Why Clojure" as they have already done a great job on that. So, I'm hoping to jump right into showing some of the lovely but shocking syntax. One of the comments that always come up from people starting to look into a Lisp dialect is the difference in syntax compared to a language that evolved from C. For myself, it did take me a bit to look past all the parentheses, but over time it does become a very elegant language to read.

{{< image src="https://imgs.xkcd.com/comics/lisp_cycles.png" alt="Lisp Cycles" position="center" style="border-radius: 8px;" >}}

[xkcd: Lisp Cycles](https://xkcd.com/297/)

For a language to compare Clojure to I'm going to pick JavaScript as it's easy for setting up examples. I also think it's much more approachable for more people than something like Java, but let's keep in mind that Clojure can target JavaScript with something called [ClojureScript](https://clojurescript.org/). If you're an active front end developer you may have seen this option available on [The State of JavaScript](https://stateofjs.com/) reports.

## TL;DR
So, as I was starting to write this posting, Uncle Bob made a pretty good summary of the Lisp syntax compared to Java on [Twitter](https://twitter.com/unclebobmartin/status/1215642524817080322),

{{< tweet user="unclebobmartin" id="1215642524817080322" >}}

I think this makes a good TL;DR section, as this is a good guiding point when thinking about Clojure.

## A Simple Start
Ok, let's start with something small. Let's add some numbers together.

```javascript
1 + 2;
```
Easy, right? Ok, let's take a look at this in Clojure

```clojure
(+ 1 2)
```
I think this needs to be broken up a bit to fully understand it

{{< image src="/images/taste-of-clojure/clojure_breaking_apart.png" alt="Clojure Function" position="center" style="border-radius: 8px;" >}}

I think the strange thing is the parentheses and the way it hugs the function that is being called and its arguments. The interesting thing is that code is represented in the list data structure, this is referred to as [Homoiconicity](https://en.wikipedia.org/wiki/Homoiconicity) and where the idea for "code as data" comes from as the code is constructed from regular Clojure data structures. This is an idea that comes from Lisp and not just something that is found in Clojure, which speaks to the rich history of Lisp.

The function that is being called follows next after the opening parentheses, along with the arguments. Besides the order of things, I think we can see that we are adding 1 to 2. Let's do something a bit more complex and add some more mathematical functions to the mix

```javascript
5 + 1 * 6
```

If you think back to your days in school where we learned about order of operations, this means we first multiply 1 and 6 together and then add 5.

So, what does something like this look like in Clojure,

```clojure
(+ 5 (* 1 6))
```

The way you would read this is very similar to the order of operations, going from the inner to outer, so multiply 1 and 6 together and then add 5. I think this brings up a good point, in Clojure, we are not relying upon order of operations to define how the code should compute, this is the order that any function would compute even if it's not a mathematical operation. I think this helps avoid common issues, for example, let's say the intent was to add 5 and 1 together and then multiply by 6.

```javascript
(5 + 1) * 6
```

And in Clojure you would have,

```clojure
(* (+ 5 1) 6)
```

I believe that Clojure gives you more consistent syntax and lets you explicitly state the order and not rely upon order of operations.

Let's go back to adding numbers, this time with more numbers. (Bare with me there's a point to this)

```javascript
1 + 2 + 3 + 4 + 5 + 6;
```

So, in Clojure we can create functions to take any number of arguments,

```clojure
(+ 1 2 3 4 5 6)
```

As you see, we can pass any length of arguments into the plus function, as simple as this may seem it is very useful and convenient. We can get the same behavior from JavaScript, so let's create some functions of our own to demonstrate in both Javascript and Clojure.

## Functions
Ok, so let's look at creating a function that does something simple. We'll make something that greets a person or a group of people. Yes, simple but I think it can demonstrate functions in Clojure.

Let's start with the most simplest part, creating a function that greets a single person.

```clojure
(def greet (fn [person]
	(str "Hello " person)))

(greet "Tony") ; => "Hello Tony"
```

What we have here is the creation of a function called `greet`, to define something we use [def](https://clojuredocs.org/clojure.core/def) with a name (or symbol to be more formal). So, we are defining an anonymous function that takes in one parameter called `person` found in the square brackets. Then we call the [str](https://clojuredocs.org/clojure.core/str) function which can take any number of arguments and concatenate them together. We also see how we can call this function, which is the same as we did with the plus operator.

Because this is so common, there is a cleaner way to create the same function which is more convenient and that is using [defn](https://clojuredocs.org/clojure.core/defn)

```clojure
(defn greet [person]
	(str "Hello " person))

(greet "Tony") ; => "Hello Tony"
```

A bit nicer and cleaner. 

Let's move on to two names to show another feature of Clojure functions.

```clojure
(defn greet
  ([person]
   (str "Hello " person))
  ([first-person last-person]
   (str "Hello " first-person ", " last-person)))

(greet "Tony") ; => "Hello Tony"
(greet "Tony" "Sarah") ; => "Hello Tony, Sarah"
```

A bit harder to read, but what this does is creates a function that provides different definitions based on how many names you're passing into it. Clojure allows you to overload methods with a different number of parameters, this is nice for building functionality like defaulting parameters or providing additional options.

Now for the final step, take in any number of names! 

```clojure
(defn greet [& names]
  (str "Hello " (clojure.string/join ", " names)))

(greet "Tony") ; "Hello Tony"
(greet "Tony" "Sarah") ; "Hello Tony, Sarah"
(greet "Tony" "Sarah" "Stacy") ; "Hello Tony, Sarah, Stacy"
```

Let's break this down! We are back to just one function definition but we have added an `&` to the parameters list. With the `&` we are now getting a list of names that we join together before adding Hello to the start.

What does this same functionality look like in JavaScript?

```javascript
const greet = (...names) => `Hello ${names.join(', ')}`

greet("Tony") // 'Hello Tony'
greet("Tony", "Sarah") // 'Hello Tony, Sarah'
greet("Tony", "Sarah", "Stacy") // 'Hello Tony, Sarah, Stacy'
```

Overall not too much difference, but let's just point out something, this is using newer syntax from ES6. JavaScript is constantly evolving and changing its syntax over time. I think this identifies one of the advantages of Clojure, new features and functionality can be added without drastically changing the syntax. Because of this you can focus on fine-tuning your skills and mastering Clojure over learning new syntax and what's coming out in the next version like JavaScript. 

## Conclusion
This posting could go on much longer providing a lot more details around the interesting syntax found in Clojure, but I just want to provide a taste to get people interested in the language and the concepts. I do hope to continue to write more about Clojure as I learn it myself but I want to end this post with another tweet from Uncle Bob that fits very well with my current thinking,

{{< tweet user="unclebobmartin" id="1214906676840669184" >}}
[Twitter Link](https://twitter.com/unclebobmartin/status/1214906676840669184)

## References
* [Understanding Homoiconicity, the Power Behind Clojure Macros](https://spin.atomicobject.com/2013/07/23/homoiconicity-clojure-macros/)
* [What I learned after writing Clojure for 424 days, straight](https://medium.com/@shivekkhurana/what-i-learned-after-writing-clojure-for-424-days-straight-8884ec471f8e)
* [Uncle Bob Martin presents Clojure (Chicago Java Users Group 2013-10-16 Meetup)](https://www.youtube.com/watch?v=SYeDxWKftfA)
* [James Gosling likes Clojure's immutable objects style : Clojure](https://www.reddit.com/r/Clojure/comments/a8allu/james_gosling_likes_clojures_immutable_objects/)
