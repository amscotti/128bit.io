---
author: Anthony Scotti
date: 2011-09-05T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Functional
- Groovy
- Howto
- Javascript
- Personal
- Python
- Ruby
- Clojure
title: Project Euler 001
url: /2011/09/05/project-euler-001/
---

Made this posting sometime ago but I've been forgetting to actually post it. When I was looking up some information on Scala I found a great video tutorial on youtube made by [MadocDoyu](http://www.youtube.com/user/MadocDoyu), [which can be found here](http://www.youtube.com/watch?v=wvD6JauveLA). In part of the video he introduces the Project Euler, this project seems really interesting. I plan on solving problems time to time using many of the languages I have looked at. I'm hoping this will keep my skills in these languages up to date.

Here is the first problem,

> If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
>
> Find the sum of all the multiples of 3 or 5 below 1000.

and here is the code to solve it,

## JavaScript
```js
const range = n => {
    _results = [];
    for (_i = 0; _i <= n; _i++) { _results.push(_i); }
    return _results;
}
console.log(range(999)
    .filter(n => (n % 3 === 0 || n % 5 === 0))
    .reduce((a, b) => a + b))
```

## Updated ES6 version
```js
console.log([...Array(1000).keys()]
    .filter(n => n % 3 == 0 || n % 5 == 0)
    .reduce((a, b) => a + b))
```

## Ruby
```ruby
puts (1...1000).find_all{ |i| i%5 == 0 || i%3 == 0 }.inject(:+)
```

## Elixir
```elixir
IO.puts 1..999 
|> Enum.filter(fn(x) -> rem(x, 3) == 0 || rem(x, 5) == 0  end) 
|> Enum.sum()
```

## Groovy
```groovy
println ((1..<1000).findAll{ i -> i%5 == 0 || i%3 == 0}.sum())
```

## Python
```python
print(sum(x for x in range(1, 1000) if (x % 3 == 0 or x % 5 == 0)))
```

## Clojure
```clojure
(->> (range 1000)
     (filter #(or (zero? (rem % 3)) (zero? (rem % 5))))
     (reduce +)
     (println))
```


Nothing too hard, I really enjoy the one liners from Groovy and Ruby and seeing them together kind of shows how similar they are. I'm not fully happy with the javascript code... I looked for a better way but I was unable to find anything using the base language. If anyone has an idea on how to make any of the code better let me know.

If you want to see how to solve this with Scala check out [MadocDoyu's videos](http://www.youtube.com/user/MadocDoyu). They are really great to watch!

**Edit**:

Based on the reply from md2perpe on Github there is a more mathematical way to solve this problem.

```
Using the formula 1 + 2 + 3 + ... + n = n*(n+1)/2 instead of a code loop.

Sum of all numbers <1000 divisible by 3:
3 + 6 + 9 + ... + 999 = 3 * (1 + 2 + 3 + ... + 333) = 3 * 333*334/2 = 166833

Sum of all numbers <1000 divisible by 5:
5 + 10 + 15 + ... + 995 = 5 * (1 + 2 + 3 + ... + 199) = 5 * 199*200/2 = 99500

Adding these up, those numbers divisible by 3*5 = 15 are counted double. Therefore we need to subtract these once:

Sum of all numbers <1000 divisible by 15:
15 + 30 + 45 + ... + 990 = 15 * (1 + 2 + 3 + ... + 66) = 15 * 66*67/2 = 33165

Thus we get the result 166833 + 99500 - 33165 = 233168.
```