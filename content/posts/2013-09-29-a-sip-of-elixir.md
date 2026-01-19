Title: A Sip of Elixir
Date: 2013-09-29 00:00
Slug: 2013/09/29/a-sip-of-elixir
Save_as: 2013/09/29/a-sip-of-elixir/index.html
URL: 2013/09/29/a-sip-of-elixir/
Tags: Elixir, Erlang, Functional
Summary: An exploration of Elixir, a functional programming language running on the Erlang VM. Discusses functional programming benefits for multi-core processing without thread safety issues, Erlang's role in enabling concurrent systems, actor model, pattern matching, and how Elixir builds on these foundations with modern syntax.

![Elixir Logo](/images/logo/elixir_logo.png)


If you've read any significant amount of my blog you've probably realized that I'm fascinated with programming languages; more precisely the syntax, the community, and the purpose of the language. [Elixir](http://elixir-lang.org/) happens to be one of these languages that has recently caught my attention.

I love the ideas functional programming brings and how you to solve problems as a result of those ideas. One of the things that functional programming is helping people to solve is how to get the most out of systems that have multiple cores. Most applications nowadays are written to use a single core with a way to achieve multi-core processing through the use of threads. The downfall of using threads is that it opens up issues due to mutable state and deadlocks. To use threads in most languages is not an easy straightforward process; this is where Erlang comes into play.

## Erlang

[Erlang](http://en.wikipedia.org/wiki/Erlang_%28programming_language%29) is a language created in 1986, which would make the language about 27 years old. So why do we care about it and how does it relate to Elixir?

Erlang has been used for sometime in systems that need high reliability. Some companies have reported to use Erlang in systems that have been able to achieve a reliability of nine "9"s. You can find Erlang still used in many online services and software for example: Databases like [CouchDB](http://couchdb.apache.org/) and [Riak](http://basho.com/riak/), and at places like Facebook and [Github](https://github.com/).

One of the strength of Erlang is support for concurrency. Erlang is able to create lightweight processes without shared state, this allows you to divide up your workload into individual processes which support being run on multi-core systems. Erlang's concurrency implementation is the [Actor model](http://en.wikipedia.org/wiki/Actor_model).

Elixir is built on top of Erlang, so all the great things that you find in Erlang you will be able to use in Elixir. The only exception is, in Elixir the syntax is more like Ruby.

## Elixir

Elixir takes aspects of Ruby and other modern languages to offer a better syntax for working on the Erlang VM. Elixir also adds some unique syntax of its own.

Elixir has all the common things that you would expect from any language, so I will show you some of the exciting parts of Elixir.

### Pattern Matching

In Elixir, the = doesn't refer to assignment as in other languages but it's used for pattern matching. Pattern matching is used all over the place for various things. One use case is for functions, based on the input, you can match what you want to happen. Think switch statements on steroids!

```elixir
defmodule Fizzbuzz do
  def match(0, 0, _), do: "Fizzbuzz"
  def match(0, _, _), do: "Fizz"
  def match(_, 0, _), do: "Buzz"
  def match(_, _, n), do: n

  def fizzbuzz(n) do
    match(rem(n, 3), rem(n, 5), n)
  end
end

Enum.each(1..100, fn(i) -> IO.puts Fizzbuzz.fizzbuzz(i) end)
```

### Anonymous Functions

Being a functional programming language, Elixir treats functions as first-class citizens. Anywhere that you can declare a String you can declare a function, even if this means from within functions.

To my joy, I find working with functions in Elixir very similar to what you find in JavaScript. This even includes having self executing functions.

```elixir
# Creating an anonymous function using the fn...end syntax
div = fn(number, divisor) -> rem(number, divisor) end

IO.puts div.(15, 3)

# Shorthand with &(...) syntax
div2 = &(rem(&1, &2))

IO.puts div2.(15, 3)

# Passing function as a parameter
add = fn(a, b) -> a + b end

Enum.reduce([1, 2, 3, 4, 5], 0, add)

# Same as before but no need to assign to a variable
Enum.reduce([1, 2, 3, 4, 5], 0, fn(a, b) -> a + b end)

# Shorthand with &(...) syntax
Enum.reduce([1, 2, 3, 4, 5], 0, &(&1 + &2))

# Self Executing anonymous function
(fn(name) -> IO.puts "Hello #{name}" end).("World")

# Self Executing with using Pattern Matching
result = case (fn(a, b) -> a + b end).(1, 2) do
  3 -> "Three!"
  _ -> "IDK"
end

IO.puts result
```

### Pipe Operator \|>

If you have worked with the Unix terminal you most likely have used | (Pipe) before. Commonly you would take the output from one command and pipe it into another. Elixir has your back and will let you do the same.

This is what you would see in most languages,

```elixir
Enum.join(Enum.filter(Enum.map(1..20, &(&1 * 2)), fn(x) -> rem(x, 3) == 0 end), ", ")
```

To understand this you have to unravel from the inner to the outer. But in Elixir, this same code can be rewritten using the pipe operator like so,

```elixir
1..20 |> Enum.map(&(&1 * 2)) |> Enum.filter(fn(x) -> rem(x, 3) == 0 end) |> Enum.join(", ")
```

This lets you think about your application as data transformation steps.

For a more details overview of the Elixir syntax checkout [Learn Elixir in Y minutes](http://learnxinyminutes.com/docs/elixir/)

Elixir also comes with a tool that is a cross between Rake and NPM (from Ruby and NodeJS respectively), it's called [Mix](http://elixir-lang.org/getting_started/mix/1.html). Mix will bootstrap your application structure for you, and will handle dependency management. Elixir also comes with a built in test framework called [ExUnit](http://elixir-lang.org/getting_started/ex_unit/1.html) which Mix is able to run.

There is one thing that I can't find much information on, how someone can deploy Elixir, or best practices for running in production. This could be due to the fact that Elixir is still in development but I was able to find a [Heroku buildpack for Elixir](https://github.com/goshakkk/heroku-buildpack-elixir) to let you push Elixir web apps to Heroku. I'm sure as time goes by the Elixir team will work on this missing part of Elixir.

## Resources
* [How I Got Started Setting Up Elixir](http://newtriks.com/2013/09/02/how-i-got-started-setting-up-elixir/)
* [Why My Next Programming Language Is Elixir](http://benjamintanweihao.github.io/blog/2013/06/08/why-my-next-programming-language-is-elixir/)
* [Meet Elixir by PeepCode](https://peepcode.com/products/elixir)
* [Elixir Sips - Learn Elixir With a Pro](http://elixirsips.com/)
* [Elixir Home Page](http://elixir-lang.org/)
