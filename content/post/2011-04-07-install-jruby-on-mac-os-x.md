---
author: Anthony Scotti
date: 2011-04-07T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Howto
- Install
- JRuby
- Mac
- Ruby
title: Install JRuby on Mac OS X
url: /2011/04/07/install-jruby-on-mac-os-x/
---

Same idea as the [Groovy and Grails posting]({{< relref "2011-03-31-install-groovy-and-grails-on-mac-os-x.md" >}}), most of the steps are the same but here they are.

Download JRuby from http://www.jruby.org/, as of writing this the latest release is 1.6.0. I'm downloading the tar file, I believe it the same as the zip file just different format used to compress the files.

```
$ cd Downloads
$ tar -xzf jruby-bin-1.6.0.tar.gz
```

Now lets move it to our /usr/share folder and make the needed symbolic link.

```
$ sudo mv jruby-1.6.0 /usr/share/
$ cd /usr/share/
$ sudo ln -s jruby-1.6.0/ jruby
```

Last step is to update your .profile file within your home folder. Just add this to the top,

```
JRUBY_HOME=/usr/share/jruby; export JRUBY_HOME
PATH=$JRUBY_HOME/bin:$PATH; export PATH
```

Close all Terminals and reopen one.  To test to see if everything is setup right, run this,

```
$ jruby -v
jruby 1.6.0 (ruby 1.8.7 patchlevel 330) (2011-03-15 f3b6154) (Java HotSpot(TM) Client VM 1.6.0_24) [darwin-i386-java]
```

To update just download the new file, move it to /usr/share folder and update the symbolic link like this,

```
$ cd /usr/share/
$ sudo rm jruby
$ sudo ln -s jruby-1.6.0/ jruby
```

Something to keep in mind when dealing with JRuby, it comes with a JRuby version of Gem which will be picked over the default Ruby Gem due to the paths. If you need to work with the Ruby Gem use the full path, /usr/bin/gem, like so "/usr/bin/gem update" to run the update.

If you have any questions or comments please post, also any suggestions on improving this are welcome.
