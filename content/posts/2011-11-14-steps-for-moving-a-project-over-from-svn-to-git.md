Title: Steps for moving a project over from SVN to Git
Date: 2011-11-14 00:00
Slug: 2011/11/14/steps-for-moving-a-project-over-from-svn-to-git/index.html
URL: 2011/11/14/steps-for-moving-a-project-over-from-svn-to-git/
Tags: Git, SVN, Tip
Summary: A guide to migrating SVN repositories to Git while preserving complete commit history. Uses git svn init and git svn fetch to import with all history, then git svn can be used to continue pushing back to SVN if needed, allowing gradual transition while maintaining compatibility.

Now that we are fully using Git at work one of my tasks has been to move some of our old projects over to using Git. There are some different ways you can go about doing this, you can simply do a SVN export of the project and make a new git repository from it. I don't prefer this method because you lose the commit history. The way below is a way to maintain all the history from the SVN repository.

```
$ mkdir projectFolder && cd projectFolder
$ git svn init https://svn.server.com/your/project/path
$ git svn fetch
```

At this point, your code should be pulling down in to your new git repository with all your code from SVN and its history. You are now all set and can start using the repository as if it was any other git repository. If you would like to push this out to a remote repository, check out my posting on "[Setting up a remote Git repository](/2011/04/03/setting-up-a-remote-git-repository/)".

git svn is a great tool that also lets you keep using SVN by letting you push updates back to the SVN repository. This is great if you are forced to use SVN at work, but would like to use Git when you work on a project.
