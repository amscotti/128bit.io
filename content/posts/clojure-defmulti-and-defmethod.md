---
title: "Clojure Defmulti and Defmethod"
date: 2021-07-26T20:53:44-04:00
draft: false
tags:
- Clojure
- Development
---

{{< image src="/images/logo/clojure_logo.png" alt="Clojure Logo" position="center" style="border-radius: 8px;" >}}

As I continue my journey with learning functional programming, I have started to explore deeper into the languages that I enjoy and do some experimenting with interesting parts of those languages. This has led me to `defmulti` and `defmethod`, enabling you to create methods that deal with different implementations that are selected by a dispatch function. This is certainly easier to see in code, but it allows you to create a function based on the return of the dispatch function that will send the parameters to another function.

Let's look at some code and break it down bit by bit, starting with the data we are working with,

```clojure
(def player {:class :druid
             :spec :balance
             :name "Sedna"})
```
This data represents a character in a game, like Dungeons and Dragons. You can think of this data being extended to hold stats like stamina and intellect, but for this simple example, this will do. Let's take this data and create a String that will display the character's attack using a unique ability from the class.

## defmulti

Now that we know what the data looks like that we will be working with, we need to think about our unique identifier, and for this data, we will be using `:class` to provide a unique identifier for we know where to dispatch to. Using our example data, this will give us `:druid` which means we can have code like this,

```clojure
(defmulti attack :class)
```

Everything starts with a `defmulti`, this sets up the function to return the unique identifier for the dispatch. In `(default attack :class)` we are using the fact that Keywords can be used as functions on Maps to pull the values. In this case, we are pulling the class from the Map and using it as the identifier. This function isn't limited to returning just Keywords, it can return anything that can be used as a unique identifier for the `defmethod`.

If you wanted to create something to work with multiple elements of the `player` Map, you could easily create a list of the values which can be used for your identifier like so,

```clojure
(defmulti attack
  (fn [character]
    (vals (select-keys character [:class :spec]))))
```
This would create an identifier that looks like `[:druid :balance]`, which can be used in the `defmethod`, but let's keep it simple and keep using just `:class` going forward.  

### Anonymous Function Syntax

This is a good place to quickly go over another excellent topic of Clojure, [Anonymous Function Syntax](https://clojure.org/guides/learn/functions#_anonymous_function_syntax) which is a shorthand for creating anonymous functions. The `fn` part of this `attack` can be made shorter and a bit easier to read using this,

```clojure
(defmulti main-spec
  #(vals (select-keys % [:class :spec])))
```

This code uses a macro that will expand this out behind the scenes into the full function for us. With the anonymous function syntax, we don't need to declare a variable name for the parameters instead using the `%` for the parameter. For the case where you have more than one parameter, you can use `%1`, and `%2`, and so on. This shorthand is lovely when creating functions to pass into other functions, such as `map` and `reduce`.

## defmethod

Now that we have our `defmulti` function created and we know what our identifiers will look like, we can start creating the `defmethod` that will be called if the identifier matches. If we look at the `defmethod` methods for `:druid`,

```clojure
(defmethod attack :druid [character]
  (str (:name character) " attacks with searing Wrath"))
```

We can see that we have the same name from the `defmulti`, which is "attack" and the next part is our identifier `:druid` so, when the function in `defmulti` returns `:druid`, it would dispatch to this `defmethod`.

### Destructuring

Let's look at another Clojure topic that helps keep code short and readable, [destructuring](https://clojure.org/guides/destructuring). Not a unique feature to Clojure but one that is awesome nonetheless, destructuring lets you pull data out of List, Vectors, and Maps when creating functions with `defn` or using `let`.  As we just need the `:name` we can easily destructure that out of the `character` Map like this,

```clojure
(defmethod attack :druid [{name :name}]
  (str name " attacks with searing Wrath"))
```
There are different formats to pull out data from Lists and Vectors, but this is an easy one for simply pulling out the character's name.

## Default for defmethod

Similar to a switch statement in other languages, there is a way to provide a default `defmethod` used when nothing matches the identifier.  You can use this with the Keyword `:default`

```clojure
(defmethod attack :default [{name :name}]
  (str name " isn't sure what they should be doing right now"))
```

## Putting it all together

Here is the code that can deal with Shamans, Druids, Mages, and Warriors, along with providing a default if the player's `:class` does not match to any handlers,

```clojure
(defmulti attack :class)

(defmethod attack :shaman [{name :name}]
  (str name " launches a mighty Lava Burst"))

(defmethod attack :druid [{name :name}]
  (str name " attacks with searing Wrath"))

(defmethod attack :mage [{name :name}]
  (str name " attacks with an explosive Fireball"))

(defmethod attack :warrior [{name :name}]
  (str name " hits with Mortal Strike"))

(defmethod attack :default [{name :name}]
  (str name " isn't sure what they should be doing right now"))

(def player {:class :druid
             :spec :balance
             :name "Sedna"})

(println (attack player))
```

Let's look at the flow of the code,
* We start with sending the `player` Map into `defmulti attack` function
* `defmulti attack` will pull the value from `:class`, which for our data will be `:druid`
* With the `:druid` identifier, we search for a `defmethod attack` that matches
* After finding `defmethod attack :druid`, the `player` Map is sent into that method
* Then we see that `Sedna attacks with searing Wrath` get printed out.

## Conclusion
We looked at `defmulti` and `defmethod`, which can be used when working on data that require different manipulation. This can let you move conditional logic into methods where you can work on the individual data in seclusion. [Clojure Docs](https://clojuredocs.org/clojure.core/defmethod) has some other examples and details which I found helpful when learning more about `defmulti` and `defmethod`.

We also briefly talked about [Anonymous Function Syntax](https://clojure.org/guides/learn/functions#_anonymous_function_syntax) as an excellent way to create small functions along with [destructuring](https://clojure.org/guides/destructuring) as ways to help make your code clean and easier to read by letting you rip data apart so you can focus on the main logic of your function. I'm hoping to find some other interesting topics for another posting as I continue exploring Clojure.