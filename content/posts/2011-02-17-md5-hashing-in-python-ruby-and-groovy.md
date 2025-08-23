Title: MD5 hashing in Python, Ruby and Groovy
Date: 2011-02-17 00:00
Slug: 2011/02/17/md5-hashing-in-python-ruby-and-groovy
Save_as: 2011/02/17/md5-hashing-in-python-ruby-and-groovy/index.html
URL: 2011/02/17/md5-hashing-in-python-ruby-and-groovy/
Tags: Groovy, MD5, Python, Ruby, Tip
Summary: Code examples for generating MD5 hashes in three programming languages. Shows both quick one-line hashing and the update method for hashing large data in chunks. Notes about using SHA-1 with salt instead of MD5 for password storage to prevent rainbow table attacks.

Hopping around from languages to languages, its easy to forget how to do something, nothing that a quick Google search can't help with but I wanted to make this posting for myself to save some time. [MD5](http://en.wikipedia.org/wiki/MD5) is used all over the place, its a one way hash that can be used for checking the integrity of files, storing passwords in databases and checking text being passed around. I do want to add a note here about using MD5 hashes for storing passwords in a database, I would start by looking at [SHA-1](http://en.wikipedia.org/wiki/Sha1) along with using salt this will help ensure if anyone gets a hold of your database they can just use [rainbow table](http://en.wikipedia.org/wiki/Rainbow_table) to workout the plain text of the password.

## Python
```python
import hashlib

#Quick MD5 of text
text = "MD5 this text!"
md5hash1 = hashlib.md5(text).hexdigest()

#MD5 of text with updates
m = hashlib.md5()
m.update("MD5 ")
m.update("this ")
m.update("text!")
md5hash2 = m.hexdigest()

#Output
print("%s should be the same as %s" % (md5hash1, md5hash2))
```

## Ruby
```ruby
require 'digest/md5'

#Quick MD5 of text
text = "MD5 this text!"
md5hash1 = Digest::MD5.hexdigest(text)

#MD5 of text with updates
m = Digest::MD5.new()
m << "MD5 "
m << "this "
m << "text!"
md5hash2 = m.hexdigest()

#Output
puts "#{md5hash1} should be the same as #{md5hash2}"
```

## Groovy
```groovy
import java.security.MessageDigest

def digest = MessageDigest.getInstance("MD5")

//Quick MD5 of text
def text = "MD5 this text!"
def md5hash1 = new BigInteger(1,digest.digest(text.getBytes())).toString(16).padLeft(32,"0")

//MD5 of text with updates
digest.update("MD5 ".getBytes())
digest.update("this ".getBytes())
digest.update("text!".getBytes())
def md5hash2 = new BigInteger(1,digest.digest()).toString(16).padLeft(32,"0")

//Output
print "${md5hash1} should be the same as ${md5hash2}"
```

So as you see from the code there are 2 ways to get a hash, one is to quickly get the hash from the text and the other is to update the digest. You would want to use the update method when you are reading a lot of data, for example a file. This will let you read part of the data and add it to the digest part by part. If you just need to check some text you can easily do so with one command.

If you have any questions or comments please post, also any suggestions on improving this are welcome.
