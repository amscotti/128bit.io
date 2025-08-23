Title: MD5 hashing in CoffeeScript, Perl and Scala
Date: 2012-04-22 00:00
Slug: 2012/04/22/md5-hashing-in-coffeescript-perl-and-scala
Save_as: 2012/04/22/md5-hashing-in-coffeescript-perl-and-scala/index.html
URL: 2012/04/22/md5-hashing-in-coffeescript-perl-and-scala/
Tags: CoffeeScript, Howto, Perl, Scala
Summary: Code examples for generating MD5 hashes in three additional programming languages. Shows both quick one-line hashing and incremental update method for large data processing. Continues series of MD5 implementations across different languages including previous Python, Ruby, and Groovy examples.

Kind of a follow up to my on [MD5 hashing in Python, Ruby and Groovy](/2011/02/17/md5-hashing-in-python-ruby-and-groovy/) posting, Here is a way of doing MD5 hashing in CoffeeScript and Perl.

## CoffeeScript/Node.js
```coffeescript
crypto = require('crypto');

#Quick MD5 of text
text = "MD5 this text!"
md5hash1 = crypto.createHash('md5').update(text).digest("hex")

#MD5 of text with updates
m = crypto.createHash('md5')
m.update("MD5 ")
m.update("this ")
m.update("text!")
md5hash2 = m.digest("hex")

#Output
console.log "#{md5hash1} should be the same as #{md5hash2}"
```

## Perl
```perl
use Digest::MD5  qw(md5 md5_hex md5_base64);

#Quick MD5 of text
my $text = "MD5 this text!";
my $md5hash1 = md5_hex( $text );

#MD5 of text with updates
$md5 = Digest::MD5->new;
$md5->add("MD5 ");
$md5->add("this ");
$md5->add("text!");
$md5hash2 = $md5->hexdigest;

#Output
print "$md5hash1 should be the same as $md5hash2\n";
```

## Scala
```scala
import java.security.MessageDigest

val digest = MessageDigest.getInstance("MD5")

//Quick MD5 of text
val text = "MD5 this text!"
val md5hash1 = digest.digest(text.getBytes).map("%02x".format(_)).mkString

//MD5 of text with updates
digest.update("MD5 ".getBytes())
digest.update("this ".getBytes())
digest.update("text!".getBytes())
val md5hash2 = digest.digest().map(0xFF & _).map("%02x".format(_)).mkString

//Output
println(md5hash1 + " should be the same as " + md5hash2)
```

I also moved the code for Python, Ruby and Groovy into the same Gist on Github. If you know a better way feel free to fork and update!
