Title: A quick look at CoffeeScript, TypeScript, and Dart
Date: 2013-08-11 00:00
Slug: 2013/08/11/a-quick-look-at-coffeescript-typescript-and-dart
Save_as: 2013/08/11/a-quick-look-at-coffeescript-typescript-and-dart/index.html
URL: 2013/08/11/a-quick-look-at-coffeescript-typescript-and-dart/index.html
Tags: CoffeeScript, TypeScript, Dart, JavaScript
Summary: Comparison of CoffeeScript, TypeScript, and Dart as JavaScript alternatives. CoffeeScript offers Ruby/Python syntax with code reduction; TypeScript is strict superset with optional typing and IDE support; Dart includes VM for server apps and optional typing with Java-like syntax. All three improve function syntax.

As more developers focus on working on the front end, more tools are created to assist the developers. We now have some great tools and IDEs to help us with our development of JavaScript. The language itself can be hard to grasp and leads to many errors and bugs in your code. New languages for the web have been emerging to help tackle the issues that people are having with building scalable JavaScript applications.

I want to give a quick comparison of the syntax of CoffeeScript, TypeScript, and Dart along with some features and disadvantages. All three take a new approach to building JavaScript applications with hopes of allowing you to scale your application, keeping in mind code quality and ease of reading.

## Quick Overview

### CoffeeScript

CoffeeScript has been around for a bit now, made by Jeremy Ashkenas (Same person behind [Backbone.js](http://backbonejs.org/) and [Underscore.js](http://underscorejs.org/)) in 2009. The syntax looks like a mix of Ruby and Python and tends to draw people with a background in those languages. CoffeeScript keeps JavaScript's best practices in mind but offers a better syntax usually with much less code. Some teams that have switched over to using CoffeeScript have noted an increase in their output. CoffeeScript support has also been included in Ruby on Rails as of version 3.1

### TypeScript

TypeScript is Microsoft's approach to solving the issues they have found with JavaScript and it's ability to scale up for large applications. TypeScript is a superset of JavaScript and is focused more on tooling to help then introducing new syntax. TypeScript adds optional typing and focus on code completion to allow an IDE to notify the developer if there are any errors. It also adds a small amount of new syntax which corresponds to ideas in ECMAScript 6. The primary IDE for TypeScript is Visual Studio but the community has made plug-ins for other editors like Sublime Text and WebStorm. Microsoft and members of the community have also done a great job of adding definitions files for popular libraries such as jQuery, Node.js, AngularJS and many more.

### Dart

Dart is Google's approach to solving issues they have found with JavaScript. Appearing in 2011, it is just releasing Beta 1. Out of all three, Dart is the most radical of them all because it isn't just a language that compiles down to JavaScript but also it is meant to run on it's own VM, Dart VM. Dart is designed for speed and building large-scale web applications, also it is able to run on the server similar to Node.JS but this is not the current focus of Dart. Dart introduces some excellent new features and syntax that still keeps compatibility with modern JavaScript VMs. The syntax is very much like Java or C#, which lends itself to easy learning if you're coming from one of those languages. Like TypeScript, Dart has optional typing to help with development. Dart also has its own IDE called the Dart Editor which has many excellent features to help developers along with plugins for other editors.

## Functions
One of the primary things that all JavaScript code has is functions. All three languages have syntax to write functions and to keep them nice and organize.

### CoffeeScript

```coffeescript
divisible = 3

divisibleReporter = (lastFound, nextDivisible) ->
  "Found: #{lastFound}, Next: #{nextDivisible}"

divisibleKeeper = ((divisible) ->
  lastFound = 0
  nextDivisible = divisible
  (number) ->
    if (number >= nextDivisible)
      nextDivisible = (Math.floor(number/divisible) + 1) * divisible
      lastFound = Math.floor(number/divisible) * divisible
      console.log divisibleReporter(lastFound, nextDivisible)
  )(divisible);

for n in [1..100]
  divisibleKeeper(n)
```

### TypeScript

```typescript
var divisible = 3;

var divisibleReporter = function(lastFound:number, nextDivisible:number){
  return "Found: " + lastFound + ", Next: " + nextDivisible;
};

var divisibleKeeper = (function(divisible:number) {
  var lastFound = 0;
  var nextDivisible = divisible;
  return function(number:number) {
    if (number >= nextDivisible) {
      nextDivisible = (Math.floor(number / divisible) + 1) * divisible;
      lastFound = Math.floor(number / divisible) * divisible;
      console.log(divisibleReporter(lastFound, nextDivisible));
    }
  };
})(divisible);

for (var i = 1; i <= 100; ++i) {
  divisibleKeeper(i);
}
```

### Dart

```dart
int divisible = 3;

String divisibleReporter(int lastFound, int nextDivisible) => "Found: ${lastFound}, Next: ${nextDivisible}";

var divisibleKeeper = ((int divisible) {
  int lastFound = 0;
  int nextDivisible = divisible;
  return (int number){
    if (number >= nextDivisible) {
      nextDivisible = ((number/divisible).floor() + 1) * divisible;
      lastFound = (number/divisible).floor() * divisible;
      print(divisibleReporter(lastFound, nextDivisible));
    }
  };
})(divisible);

void main() {
  for (var i = 0; i < 100; i++) {
    divisibleKeeper(i);
  }
}
```

Nothing too dramatic from TypeScript, but you get a lot of help from using types. If you were to come back and look at this code after a bit, you would know what types your functions need and your IDE would inform you if you made a mistake.

You find something similar within Dart using types, but Dart has some tricks for dealing with small functions. If you are writing one-line functions you are able to use => (fat arrow) and there is no need to wrap it around with brackets. I was impressed that Dart was able to allow a self executing function along with its ability to use lexical closures. This is something that I take use of in JavaScript to encapsulate data and functionality. It's also nice to know that Dart is capable of doing this as well.

CoffeeScript takes a more dramatic approach by completely removing the function keyword and brackets from the function definition and uses ->.

## Classes
With JavaScript being a [Prototypical language](http://en.wikipedia.org/wiki/Prototype-based_programming) there are no Classes but luckily you can imitate classes quite well in JavaScript. The syntax's quite rough and untraditional if you're coming from object-oriented languages. CoffeeScript, TypeScript, and Dart has their own syntax for dealing with classes as shown below.

### CoffeeScript

```coffeescript
class Actor
  constructor: (@firstName, @lastName, @start, @end) ->

  info: ->
    fullname = "#{@firstName} #{@lastName}"
    "#{fullname} was from #{@start} to #{@end}"

class TimeLord
  constructor: (@name, @companions = []) ->

  addCompanion: (companion) ->
    @companions.push companion

doctorWho = [
  ["Christopher Eccleston", 2005, 2005]
  ["David Tennant", 2005, 2010]
  ["Matt Smith", 2010, 2013]
]

doctors = (new Actor(doc[0].split(' ')[0], doc[0].split(' ')[1], doc[1], doc[2]) for doc in doctorWho)
for doc in doctors
  console.log doc.info()

theDoctor = new TimeLord 'The Doctor'
theDoctor.addCompanion 'Rose Tyler'
theDoctor.addCompanion 'Martha Jones'
theDoctor.addCompanion 'Donna Noble'
console.log theDoctor
```

### TypeScript

```typescript
class Actor {
  firstName: string;
  lastName: string;
  start: number;
  end: number;

  constructor(firstName: string, lastName: string, start: number, end: number) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.start = start;
    this.end = end;
  }

  info() {
    var fullname = this.firstName + " " + this.lastName;
    return fullname + " was from " + this.start + " to " + this.end;
  }
}

class TimeLord {
  name: string;
  companions: string[];

  constructor(name: string, companions: string[] = []) {
    this.name = name;
    this.companions = companions;
  }

  addCompanion(companion: string) {
    this.companions.push(companion);
  }
}

var doctorWho = [
  ["Christopher Eccleston", 2005, 2005],
  ["David Tennant", 2005, 2010],
  ["Matt Smith", 2010, 2013]
];

var doctors: Actor[] = [];
for (var i = 0; i < doctorWho.length; i++){
  var names = (<string>doctorWho[i][0]).split(" ");
  doctors.push(new Actor(names[0], names[1], <number>doctorWho[i][1], <number>doctorWho[i][2]));
}

for (var j = 0; j < doctors.length; j++) {
  console.log(doctors[j].info());
}

var theDoctor: TimeLord = new TimeLord("The Doctor");
theDoctor.addCompanion("Rose Tyler");
theDoctor.addCompanion("Martha Jones");
theDoctor.addCompanion("Donna Noble");
console.log(theDoctor);
```

### Dart

```dart
class Actor {
  String firstName, lastName;
  int start, end;

  Actor(this.firstName, this.lastName, this.start, this.end);

  String info() {
    var fullname = "${firstName} ${lastName}";
    return "${fullname} was from ${start} to ${end}";
  }
}

class TimeLord {
  String name;
  List<String> companions;

  TimeLord(this.name, [this.companions]) {
    if (companions == null) {
      companions = [];
    }
  }

  void addCompanion(String companion) {
    companions.add(companion);
  }
}

void main() {
  var doctorWho = [
    ["Christopher Eccleston", 2005, 2005],
    ["David Tennant", 2005, 2010],
    ["Matt Smith", 2010, 2013]
  ];

  var doctors = doctorWho.map((doc){
    var names = doc[0].split(" ");
    return new Actor(names[0], names[1], doc[1], doc[2]);
  });

  for (var doc in doctors) {
    print(doc.info());
  }

  var theDoctor = new TimeLord("The Doctor");
  theDoctor.addCompanion("Rose Tyler");
  theDoctor.addCompanion("Martha Jones");
  theDoctor.addCompanion("Donna Noble");
  print(theDoctor.companions);
}
```

Overall the structure is very similar between all three examples. You do see the advantages of using CoffeeScript to do more in less lines but Dart isn't too far behind. On the technical side of things I would say Dart has a bit of an advantage as it is naturally an object-oriented language and not imitating to be one like JavaScript.

## Conclusion
Each language has their own unique features that they add to assist with development. I'm hoping to just give you a taste and let you explore more into the language which best suits you. This is the first time that I gave TypeScript a good look over and I can see the appeal of it. Out of all three languages TypeScript would be the easiest to integrate into an existing code base. I do feel the community has done excellent job in developing plug-ins and TypeScript definitions files. As I do love the syntax of CoffeeScript, after writing this posting I feel somewhat partial to TypeScript and may look into using it on some projects that already has a large JavaScript code base.

## tl;dr

**CoffeeScript**: If you come from a Ruby or Python background you most likely will enjoy the syntax that CoffeeScript has to offer. Also if you're trying to speed up your development by typing less code CoffeeScript is a good pick.

**TypeScript**: If you want a language that does not change the syntax too much but offers a lot of tooling to the developer then TypeScript is a good pick for you. Also, if you have tons of JavaScript code already written then TypeScript is the easiest out of the three to start integrating.

**Dart**: If you're looking for a new language that is similar to Java or C# and that is built for speed, Dart is a good pick. If Google is successful, the Dart VM will be integrated into Chrome and maybe later into other browsers. At that point, any code that you have written will no longer need to be compiled into JavaScript, it would be run directly on the Dart VM to get an additional speed boost.

## Resources

### CoffeeScript
* [CoffeeScript Home Page](http://coffeescript.org)
* [The Absolute Beginner’s Guide to CoffeeScript](http://blog.teamtreehouse.com/the-absolute-beginners-guide-to-coffeescript)
* ['Meet CoffeeScript' Video from PeepCode](https://peepcode.com/products/coffeescript)

### TypeScript
* [TypeScript Home Page](http://www.typescriptlang.org)
* [TypeScript Definitions](http://www.tsdpm.com)
* [TypeScript: Application-Scale JavaScript](http://channel9.msdn.com/Events/Build/2013/3-314?utm_source=javascriptweekly&utm_medium=email)

### Dart
* [Dart Home Page](http://www.dartlang.org/)
* [Introducing Dart](http://www.youtube.com/watch?v=5KlnlCq2M5Q)
* [Dart in Action by Chris Buckett](http://www.manning.com/buckett)
* [Dart: Up and Running by Kathy Walrath and Seth Ladd](http://shop.oreilly.com/product/0636920025719.do)
