---
author: Anthony Scotti
date: 2011-07-13T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Howto
- Install
- Mac
- Scala
title: Installing Scala on Mac OS X
url: /2011/07/13/installing-scala-on-mac-os-x/
---

One of the other things I'm trying to learn on my free time is Scala, like Groovy it's a language that runs on top of the JVM and is both a object-oriented and functional programming language. One of the biggest places I know where its being used is [Foursquare](https://foursquare.com/)

Same idea as the other postings I did for installing [Groovy, Grails]({{< relref "2011-03-31-install-groovy-and-grails-on-mac-os-x.md" >}}) and [jRuby]({{< relref "2011-04-07-install-jruby-on-mac-os-x.md" >}}).

Head to the Scala home page at [http://www.scala-lang.org](http://www.scala-lang.org) and click on the '[Download Scala](http://www.scala-lang.org/downloads)' which is on the right side of the page. Download the [scala-2.9.0.1.tgz](http://www.scala-lang.org/downloads/distrib/files/scala-2.9.0.1.tgz) (which is the latest as of writing this posting).

If you just want to download it from the command line,

```
$ curl -O http://www.scala-lang.org/downloads/distrib/files/scala-2.9.0.1.tgz
```

If you want to ensure the file is downloaded correctly checkout the MD5 file.
```
$ curl http://www.scala-lang.org/downloads/distrib/files/scala-2.9.0.1.tgz.md5
10d01410fd75019fa21a88964462a077
$ md5 scala-2.9.0.1.tgz MD5 (scala-2.9.0.1.tgz) = 10d01410fd75019fa21a88964462a077
```

Now that we have the file we need to untar it, move it /usr/share and make the link to Scala for it.
```
$ tar -xzf scala-2.9.0.1.tgz
$ sudo mv scala-2.9.0.1 /usr/share/
$ sudo ln -s scala-2.9.0.1/ scala
```

Last step is to update your .profile file within your home folder. Just add this to the top:
```
SCALA_HOME=/usr/share/scala; export SCALA_HOME
PATH=$SCALA_HOME/bin:$PATH; export PATH
```

Close all Terminals and reopen one. To test to see if everything is setup right, run this:
```
$ scala

Welcome to Scala version 2.9.0.1 (Java HotSpot(TM) 64-Bit Server VM, Java 1.6.0_24).
Type in expressions to have them evaluated.
Type :help for more information.

scala>
```

After all this you should be all set to start working with Scala. If the time comes and you want to upgrade, all you need to do is download, unzip and move to /usr/share folder and update the symbolic link like so:
```
$ cd /usr/share/
$ sudo rm scala
$ sudo ln -s scala-2.9.0.1/ scala
```

If you have any questions or comments please post, also any suggestions on improving this are welcome.
