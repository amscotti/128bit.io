Title: Optional Types and Pipes in F#
Date: 2020-09-10 17:24
Slug: optional-types-and-pipes-in-fsharp
Tags: FSharp, Dotnet, Development
Summary: Code challenge demonstrating F# features including pipe-forward operator and discriminated unions. Shows returning None or Some option when finding first unique character, and using DiscriminatedUnions to implement class-specific behavior with overrides, highlighting optional types as better pattern for handling values that may or may not be present.

For this first topic of showing off parts of F# I want to use a code challenge I have used for interviewing candidates at a couple different companies. This challenge is simple to solve but is left open ended to allow the candidate to discuss and debate the decisions they have made. The main point of the challenge isn’t the coding, but it does provide us with an example to show off optional types and pipe operator in F#.

So, here is the rules of the challenge, 

Write a function that returns the first unique character in a given string. For example, 
* Given "abc" "a" will be returned
* Given "aabc" "b" will be returned
* Given "aabbc" "c" will be returned
* Given "aabbcc" return a null or whatever best represents the lack of a unique character in your language.

As said before, this is an open ended challenge that can be solved in many different ways which is part of the charm of the challenge.

## Optional Types
One of the key things I made sure to add to the challenge is the "whatever best represents the lack of a unique character in your language" part, and this was mostly for languages that had "Maybe" or Optional Types. Maybes are a type of monad, which is a topic from mathematics that was re-discovered in computer science with functional programming languages. Exactly what is a monad is outside of this posting as it is a vastly larger topic within itself. For now, I think it’s best to think of the Optional Types as data that has two different states, `Some` or `None`. This makes Optional Types a [Discriminated Unions](https://docs.microsoft.com/en-us/dotnet/fsharp/language-reference/discriminated-unions), which would be defined like so:

```fsharp
type Option<'a> = 
   | Some of 'a
   | None
```

In the case of this challenge we will be returning a `char option` (or `option<char>` option of type `char`). This means we will have an option that could have **some** character or **none**. Because one of the cases in the challenge is the ability to represent a case without finding a unique character I feel the option type is a good match for this challenge. Seeing many solutions to this challenge most people simply return a null, leaving the user of your function to take on the responsibility to remember to check for a null when using the return. 

Optional Types provide a better mechanic than returning null and removes the need to check before using the return. Using Optional Types in F# means you need to unwrap the data out of the option type before you are able to use it, and the compiler will enforce this as well. I think needing to handle the possibility that nothing may be returned from this function helps deal with negative cases right away without forgetting about them.

There are many ways of getting data out of an option, but I have mostly been using [Pattern Matching ](https://docs.microsoft.com/en-us/dotnet/fsharp/language-reference/pattern-matching) with the [Match expressions](https://docs.microsoft.com/en-us/dotnet/fsharp/language-reference/match-expressions). Pattern Matching in F# is very powerful and lets you check for a lot of different states of data, for example being able to break lists apart or being used in combination with [Discriminated Unions](https://docs.microsoft.com/en-us/dotnet/fsharp/language-reference/discriminated-unions), which is what we will be doing for the Optional Types.

Let’s see what it looks like to use match for the return of our function, and for now forget about the implementation `firstUnique`. 

```fsharp
let firstUnique (input: string): char option = ???

let main argv =
	firstUnique "abc" with
    | Some c -> printfn "First unique letter is '%c'" c
    | None -> printfn "Didn't find any unique letter"
```

The two main parts of the match expression are `Some c` and `None`, you can think of this as an advanced switch statement. For the path of `Some` we are initializing a variable call `c` which will hold the character that is wrapped in the `Some`. If we don’t have a character, we will be using the `None` path. 

This is a simple example, the same thing could be achieved in other languages using null but F# enforces this behavior with the compiler but also provides tools to extend this functionality. Using Optional Types and the ideas found in F#, you can avoid null pointer exception and create stable code that is able to handle both positive and negative cases.

## Pipe operator
The Pipe operator `|>` (or more precisely called Pipe Forward) in F# is a very popular piece of syntax, it has been copied into other languages like Elm and Elixir and is even a proposal to be added to [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Pipeline_operator). I’ve actually talked about the pipe operator previously in my [Elixir posting back in 2013](/2013/09/29/a-sip-of-elixir/). The Pipe operator is just [syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar) making the code easier to read and understand due to letting you change the order of the code but still maintain the same operations. 

Let’s take the same problem from [Project Euler](https://projecteuler.net/) used in the Elixir posting, 

> If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

This is what the code looks like without using the Pipe operator,
```fsharp
List.sum (List.filter (fun x -> x % 3 = 0 || x % 5 = 0) [1..999])
```
It’s readable in this short example but as more things are needed I can see this being a bit harder to understand, to the point that you most likely would start breaking things out into steps by using variables.

With using the Pipe operator,
```fsharp
[1..999] 
|> List.filter (fun x -> x % 3 = 0 || x % 5 = 0) 
|> List.sum
```
With the `|>` you more or less break things out into steps making it cleaner and easier to understand. Many times this is compared to the UNIX pipe operator because it shares a lot of the same functionality.

F# has a lot more operators to help keep code easier to read, there is the `<|` which is the Pipe Backward working pretty similar to Pipe Forward but, backwards. There is also `>>` and `<<` which are used for function composition, to combine two functions together.

## Complete Example
I think we have the basic ideas needed to understand the solution that I came up with for the challenge.

```fsharp
let firstUnique (input: string): char option =
    input 
    |> Seq.countBy id 
    |> Seq.filter (snd >> (=) 1)
    |> Seq.map fst
    |> Seq.tryHead
```

This is where the Pipe operator really shines, we can see what is going on step by step by looking at the pipes.

First, `Seq` stands for [Sequences](https://docs.microsoft.com/en-us/dotnet/fsharp/language-reference/sequences) which is a data type like a list or an array with some unique properties. Sequences can provide better performance in some use cases but for this code you can think of it as the same as a list. By piping our String input of `input` into a `Seq` function F# will convert the String into a sequence of characters.

`Seq.countBy` will count the items in the sequence by a given function, in this case we are using the `id` or the identity function that will count the items in the sequence by the character. For an input of `"aabc"` we get a new sequence of tuples, of `<char * int>` type. It looks like this,

```fsharp
seq [('a', 2); ('b', 1); ('c', 1)]
```

At this point we only care about the items that have a count of 1 and this is where `Seq.filter` comes along. We want to filter tuples that only have a count of one in the second spot. `(snd >> (=) 1)` is a bit confusing, but this is creating a function that returns a boolean that will be used in the filter on each individual item in the sequence. This function uses the `snd` to pull the second item out of the tuple and compares that with a function to see if that output is equal to one. A long form of this function using a lambda would be something like this, 

```fsharp
Seq.filter (fun x -> snd x = 1)
```

After filtering the sequence, we have something that looks like this.
```fsharp
seq [('b', 1); ('c', 1)]
```

The `a` has been dropped because it has a count of two. At this point we have all the unique characters from the input, but we do need to get the data into a bit of a different format. Now that we have the data we want, we just want the characters without the counts, and we can use `Seq.map fst` which is very much like the `snd` but will take the first item from the tuple and return that as part of a new sequence. This gives us something that looks like this,

```fsharp
seq ['b'; 'c']
```

Now we have a sequence of the unique characters, and we just need to select the first character in the sequence. Using `Seq.head` will return the first item in the sequence. This is good until you think of the situation where this sequence may be empty. This is why I’m using `Seq.tryHead` which will return an `char option` which gives us a nice return for the case of having no unique characters in the input.

A lot has been compacted into this small code example, but I think it shows off the use of Optional Types and Pipes quite well along with introducing a bit more of the F# syntax. I have solved this exact same problem in many different languages just to experience what they have to offer, and this is probably one of my favorite solutions to the code challenge. I feel that it has a fair balance between being condensed but still readable mostly thanks to the pipe operator. 

I have created a project on [GitHub](https://github.com/amscotti/FirstUnique) that shows off all this code, with [unit testing](https://github.com/amscotti/FirstUnique/blob/main/FirstUnique.Tests/Tests.fs) and [command line](https://github.com/amscotti/FirstUnique/blob/main/FirstUnique.CommandLine/Program.fs) interface. Feel free to poke at it, as I’m sure there are some ways to improve the project.