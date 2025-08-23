Title: Homebrew for OS X
Date: 2012-08-26 00:00
Slug: 2012/08/26/homebrew-for-os-x
Save_as: 2012/08/26/homebrew-for-os-x/index.html
URL: 2012/08/26/homebrew-for-os-x/
Tags: Mac
Summary: A recommendation for Homebrew as package manager for Mac OS X, offering easier installation of software than manual downloads. Explains how Homebrew manages dependencies and library locations under /usr/local, making it simple to install, update, and remove packages with single commands like brew install and brew uninstall.

In past postings I have shown you how to install things like Groovy, Grails and Scala on OS X. The postings are still a good resource to use to install what you want, but if you need to install tons of things on to your system there is a better way. This is where Homebrew comes in to play.

Homebrew is said to be “The missing package manager for OS X”. If you have ever played around with a Linux or BSD system before you know they all have some kind of package manager system built in. Sadly OS X doesn’t have something like this.

Homebrew reminds me a lot of `apt-get` from Debian based systems like Ubuntu. It lets you `brew install software` and will then download the software along with all the needed dependencies to install the software. It will compile the software on your system. If you need to get your Dev environment all set, you can just string together all the software you need like, `brew install tomcat mysql groovy grails` and then you are all set to go.

Homebrew also lets you keep your software update by running `brew update` then `brew upgrade`.

Installing Homebrew is easy, all you have to do is copy this line `ruby <(curl -fsSkL raw.github.com/mxcl/homebrew/go)` in to your terminal prompt and the script will explain what is happening.

Homebrew is Ruby based, even the Formula which tells Homebrew how to install the software is in Ruby. This makes it very easy to write your own or even update preexisting Formulas. There are commands that will help with this along with all the [Formulas being on Github](https://github.com/mxcl/homebrew/tree/master/Library/Formula).

Questions or comments please feel free to post.
