Title: MD5 hashing in Dart
Date: 2013-05-04 00:00
Slug: 2013/05/04/md5-hashing-in-dart
Save_as: 2013/05/04/md5-hashing-in-dart/index.html
URL: 2013/05/04/md5-hashing-in-dart/index.html
Tags: Dart
Summary: Dart code examples for MD5 hashing using dart:crypto library. Shows both quick single-line hashing and incremental update method for streaming data, continuing series of MD5 implementations across multiple programming languages (Python, Ruby, Groovy, CoffeeScript, Perl, Scala).

Here is some Dart code for doing MD5, though at this point in time, MD5 is becoming obsolete in favor of SHA1. But as I have done code for MD5 in other languages I figured I would duplicate the code for another comparison. To look at the languages, checkout [MD5 hashing in Python, Ruby and Groovy](/2011/02/17/md5-hashing-in-python-ruby-and-groovy/) and [MD5 hashing in CoffeeScript, Perl and Scala](/2012/04/22/md5-hashing-in-coffeescript-perl-and-scala/).

```dart
import 'dart:crypto';

void main() {

  //Quick MD5 of text
  var text = "MD5 this text!";
  var md5hash1 = CryptoUtils.bytesToHex((new MD5()..add(text.codeUnits)).close());

  //MD5 of text with updates
  var m = new MD5();
  m.add("MD5 ".codeUnits);
  m.add("this ".codeUnits);
  m.add("text!".codeUnits);
  var md5hash2 = CryptoUtils.bytesToHex(m.close());

  //Output
  print("${md5hash1} should be the same as ${md5hash2}");
}
```

I do like how you can use [Method Cascades](http://tmblr.co/Zl1k2ujH3EsC), this is something that I really wish Java had in it because the code is much cleaner in my opinion.

I am hoping to have some time to play around with Dart's Isolates. It is like a cross between JavaScript's [Web Worker](http://www.html5rocks.com/en/tutorials/workers/basics/) and [Erlang or Scala actors](http://savanne.be/articles/concurrency-in-erlang-scala/).

Got a way to make the code better? Fork the Gist or comment on Github.