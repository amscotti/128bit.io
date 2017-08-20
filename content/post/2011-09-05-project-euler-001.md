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

{{< gist amscotti 1065018 "projecteuler_001.js" >}}

## Ruby

{{< gist amscotti 1065018 "projecteuler_001.rb" >}}

## Groovy

{{< gist amscotti 1065018 "projecteuler_001.groovy" >}}

## Python

{{< gist amscotti 1065018 "projecteuler_001.py" >}}

Nothing too hard, I really enjoy the one liners from Groovy and Ruby and seeing them together kind of shows how similar they are. I'm not fully happy with the javascript code... I looked for a better way but I was unable to find anything using the base language. If anyone has an idea on how to make any of the code better let me know. I posted this on github as a gist and can be found here [http://bit.ly/iNH5Pm](http://bit.ly/iNH5Pm)

If you want to see how to solve this with Scala check out [MadocDoyu's videos](http://www.youtube.com/user/MadocDoyu). They are really great to watch!

**Edit**:

Based on the reply from md2perpe on Github there is a more mathematical way to solve this problem.
