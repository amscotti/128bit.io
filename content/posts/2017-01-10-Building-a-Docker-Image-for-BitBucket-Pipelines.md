---
author: Anthony Scotti
date: 2017-01-10T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- BitBucket
- Docker
- Alpine
- Ruby
- Java
title: Building a Docker Image for BitBucket Pipelines
url: /2017/01/10/Building-a-Docker-Image-for-BitBucket-Pipelines/
---

I said in my last posting that I could do better with cutting down the build time. To get everything working I needed to add a lot of tasks to the BitBucket pipeline. Besides the execution time, BitBucket also needed to download the Docker Image every time, so the Docker Image size is also a factor in the overall build time. Let’s look at some things we can do to make a better Docker image to cut down the build time for the blog.

Let's find a new base Docker image to work with. The [ruby:2.1.7](https://hub.docker.com/r/library/ruby/tags/) is about 273 MB, the image is based on Ubuntu and comes with a lot of extra things we do not need, if we use something like the [Alpine](https://hub.docker.com/r/library/alpine/tags/) Docker images we start with a base image of 2 MB. The advantage of using an [Alpine](https://alpinelinux.org/) Docker image is we still have a package management system we can use at the reduced size. This will give us a good start and cut down the time needed to download the Docker image onto BitBucket systems.

So, we are starting with a clean image meaning we need to install `ruby`, `nodejs`, and `java`. Luckily we can just use Alpine’s package management system to install `ruby` and `nodejs`. Sadly, Java is a bit more of an issue because it needs additional packages to be installed, so after doing some online research I found a posting from Atlassian’s blog about installing Java on Alpine, [https://developer.atlassian.com/blog/2015/08/minimal-java-docker-containers](https://developer.atlassian.com/blog/2015/08/minimal-java-docker-containers). I made some changes as the posting was a bit old and some packages have been moved around. You can see the final result below. One last thing I did to help cut down on the build time was pre-install all the needed Ruby Gems. This was done by copying the `Gemfile` and `Gemfile.lock` and running `bundle install`.

After creating the `Dockerfile`, I saved it into the same repository as my blog and added the repository to Docker Hub to build the image.

Here is the full `Dockerfile`,

{{< gist amscotti bcece7b64231c6d1e9ef1995a5848e03 >}}

[https://gist.github.com/amscotti/bcece7b64231c6d1e9ef1995a5848e03](https://gist.github.com/amscotti/bcece7b64231c6d1e9ef1995a5848e03)

I updated the `bitbucket-pipelines.yml` to start using the newly created Docker Image. With this Docker Image, the `bitbucket-pipelines.yml` becomes a lot simpler now because we no longer need to install anything, it’s now just a task of building and pushing the files to S3.

{{< gist amscotti 9b133eaa192c39f83dcb4c96752a3d15 >}}

[https://gist.github.com/amscotti/9b133eaa192c39f83dcb4c96752a3d15](https://gist.github.com/amscotti/9b133eaa192c39f83dcb4c96752a3d15)

After all the updates, the image size is now at 135 MB and has more pre-installed software and the build time is at 32 sec, which is down from about 8 mins. So, overall building our own Docker image has been a win! Being able to use any image, including your own, from Docker Hub with BitBucket Pipelines is a really nice feature and one I can see being very useful for building various projects.
