Title: Install Groovy and Grails on Mac OS X
Date: 2011-03-31 00:00
Slug: 2011/03/31/install-groovy-and-grails-on-mac-os-x
Save_as: 2011/03/31/install-groovy-and-grails-on-mac-os-x/index.html
URL: 2011/03/31/install-groovy-and-grails-on-mac-os-x/
Tags: Grails, Groovy, Howto, Install, Mac
Summary: Step-by-step guide for installing Groovy and Grails on Mac OS X with symbolic links for easy upgrades. Covers downloading binary releases, moving to /usr/share, creating symbolic links to simplify version changes, updating .profile with GROOVY_HOME and GRAILS_HOME environment variables and PATH settings, and verifying installation.

Just some steps to get people up and running with Groovy/Grails on Mac OS. Hopefully with this steps you will be able to easily upgrade to any new version that comes out. Keep in mind you will need to replace the version number that is part of the file names as they upgrade.

Download the newest releases of Groovy and Grails,

*  Groovy can be found at [http://groovy.codehaus.org/](http://groovy.codehaus.org/), and as I'm writing this the Stable Release is 1.7.10. You're going to want to download the 'Binary Release'
*  Grails can be found at, [http://www.grails.org/](http://www.grails.org/) and 1.3.7 is the lastest release.

After both are downloaded open up your Terminal, this can be found under in the Utilities folder within the Applications folder.

Terminal should start you in your home folder (which is /Users/&lt;username&gt;), we are going to move to the download folder and unzip the 2 files we just downloaded.

```
$ cd Downloads/
$ unzip groovy-binary-1.7.10.zip
$ unzip grails-1.3.7.zip
```

With the 2 files unzipped we are going to move them to the /usr/share folder, and then make a symbolic link and then update your .profile with the needed path info. To move the files into the /usr/share folder we are going to need to use sudo which will ask for your user's password.

```
$ sudo mv groovy-1.7.10 /usr/share/
$ sudo mv grails-1.3.7 /usr/share/
$ cd /usr/share/
$ sudo ln -s groovy-1.7.10/ groovy
$ sudo ln -s grails-1.3.7/ grails
```

The symbolic link will make things easier when updating to any new releases, you will not need to edit your profile with any new path info and if you need to downgrade for any reason all you have to do is reset the symbolic link to point to the old folder. Now you just need to add the path info within your .profile file that can be found within your home folder (If you don't have a .profile in your home folder, then you can just make one). You are able to use any text editor you want you just need to add this to the top of the file,

```
GROOVY_HOME=/usr/share/groovy; export GROOVY_HOME
PATH=$GROOVY_HOME/bin:$PATH; export PATH
```

```
GRAILS_HOME=/usr/share/grails; export GRAILS_HOME
PATH=$GRAILS_HOME/bin:$PATH; export PATH
```

Save, close any Terminals that are open and open a new one. To test things out try running this from within the Terminal.

```
$ groovy -v
Groovy Version: 1.7.9 JVM: 1.6.0_24
$ grails
Welcome to Grails 1.3.7 - http://grails.org/
Licensed under Apache Standard License 2.0
Grails home is set to: /usr/share/grails
```

`No script name specified. Use 'grails help' for more info or 'grails interactive' to enter interactive mode`

After all this you should be all set to start working with Groovy and Grails. If the time comes and you want to upgrade, all you need to do is download, unzip and move to /usr/share folder and update the symbolic link like so.

```
$ cd /usr/share/
$ sudo rm groovy
$ sudo ln -s groovy-1.7.10/ groovy
```

If you have any questions or comments please post, also any suggestions on improving this are welcome.
