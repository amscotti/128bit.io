---
author: Anthony Scotti
date: 2011-04-03T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Git
- Howto
- Repository
- SSH
title: Setting up a remote Git repository
url: /2011/04/03/setting-up-a-remote-git-repository/
---

I been trying to use Git more and more to help me learn it.  My first step was using it for the pre on this blog but I have also been using it on some small projects I been work on for myself. Git works just fine locally and still is able to use all the features it has but to really take advantage of Git you need to setup a remote repository and here is how to do it.

Git doesn't really have a preference if the repository is hosted on some server or it it is just a USB flash drive that you carry around with you. They are both the same and will let you share your pre.

Let's make a new local repository to give us something to play around with,

```
$ mkdir test_repository
$ cd test_repository/
$ git init
Initialized empty Git repository in /Users/ascotti/Documents/test_repository/.git/
$ echo "This is my test repository" >> test.txt
$ git add .
$ git commit -m "first commit"
[master (root-commit) 05c89a0] first commit
1 files changed, 1 insertions(+), 0 deletions(-)
create mode 100644 test.txt
```

Now we have a local repository that we can test with, now lets make the remote repository. For this I'm going to use my linux server with SSH. Git is able to leverage SSH along with the linux file permissions which means by using it you have built in permissions in your remote repository. You will need Git installed on the remote server to be able to setup the repository. You can also use a USB flash drive if you want to move your pre that way. In the end they will both act the same. What needs to happen is you need to make a Git bare repository which will store all the Git data and files but is not a working copy of your pre
, this means that you need to clone from the repository if you want to work on any files. Good habit to get into anyways.

After SSH into the remote server run this,

```
$ git init --bare ~/git/test_repository.git
Initialized empty Git repository in /home/ascotti/git/test_repository.git/
```

I'm just making the remote repository within my home folder on the server as I'm the only one going to work on this project but if you are planing on using this remote repository for a group project you will want to look into also using the --shared flag in the command. This will ensure that all the files within the repository are all owned by the same group and will only let a user within that group push and pull from the repository.

Now that the remote repository is setup we need to push our local repository into it.

`$ git push ssh://dodo/~/git/test_repository.git "*:*"`

You are also able to add port number within the command if you are running SSH on a different port, like so "git push ssh://dodo:2288/~/git...". The "*:*" will push all the branches you have in your local repository to the remote repository. To make the push easier you can add the server to your list of remote repositories.

```
$ git remote add dodo ssh://dodo/~/git/test_repository.git
$ git push dodo
Everything up-to-date
```

If you are using SSH for your remote repository, keep in mind that you can setup SSH keys to make pushing and pulling even easier. Here is a post about [how to make and use SSH keys]({{< relref "2010-04-10-making-and-using-ssh-keys.md" >}}).

You are now all set to clone the remote repository and start working on any other system you may be on. I hope anyone looking into using Git finds this helpful I'm still learning myself so if anyone know of a better way please let me know.
