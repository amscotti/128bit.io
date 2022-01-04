---
author: Anthony Scotti
date: 2017-01-01T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- GitHub
- BitBucket
- Howto
- Codeship
- Ruby
- Java
title: Quick look into BitBucket Pipelines
url: /2017/01/01/Quick-look-into-BitBucket-Pipelines/
---

Atlassian just took their [Bitbucket Pipelines out of Beta](http://blogs.atlassian.com/2016/10/scaling-in-bitbucket-cloud-new-features-and-reliability-numbers/) a bit ago, so I wanted to take look and get something up and running on it.

From a quick look, it reminds me a lot of [Codeship](https://codeship.com/), which is a great service I have used to publish this blog along with using it at my previous job. For a nice test, I wanted to see if I could replace Codeship with Bitbucket Pipelines for my blog.


![Import Code](https://d2mxuefqeaa7sj.cloudfront.net/s_06A9797600B2D8A99E9F70E543B989C1AD71FC664E4241A51220BD273F2B798E_1478376083167_image.png)


The first thing for me to do was to get my blog repository imported into Bitbucket. Atlassian makes this easy by having an [import option on their website](https://confluence.atlassian.com/bitbucket/import-or-convert-code-from-an-existing-tool-795937450.html). I did find the layout in Bitbucket a bit odd at first, you have teams, projects, and then repositories. One more level than you find on Github. After thinking about this layout, it did start to make some sense to me as I scroll past tons of repositories in Github’s layout.

After importing was all set, it was time to turn on pipelines. You will then be asked to make a  `bitbucket-pipelines.yml` file in your repository, this will hold details for your build and deployment. For me, making this file part of the repository gave me a good feeling, I really like the idea of having the details of your build saved with the code.


![Environment Variables](https://d2mxuefqeaa7sj.cloudfront.net/s_06A9797600B2D8A99E9F70E543B989C1AD71FC664E4241A51220BD273F2B798E_1478376238217_image.png)


Environment variables are very easy to setup, BitBucket gives you a nice interface to provide variables that will be pushed into your container at build time. If you are working with many people on a project but don’t want them to be able to see keys for production or other services BitBucket will let you add the environment variables as “secured”. This will ensure no one is able to see them after being added. This is one feature that you will not find in Codeship.

So, this blog uses Jekyll (for now) and is hosted on S3 & CloudFront by using the `s3_website` gem. s3_website is a great little tool for publishing any static site to S3 & CloudFront but it is a bit of a pain as it needs Java to run. We’ll go into more details of this later.

I have locked down the gem versions for Jekyll, and s3_website, this is part of a  `Gemfile`  that allows me to use bundler to get them easily installed. This all works fine on Codeship bit moving to Bitbucket Pipelines I did have some issues to fix. The systems on Codeship have more software built-in giving a complete feel with less need for configuration. The Bitbucket Pipelines uses Docker Images that you can find on Docker Hub, which is really nice but missing some of the software I need.

The first issue, I’m missing a Javascript engine. Codeship comes with NodeJS pre-installed on their system, so Jekyll is able to use NodeJS without the need of installing anything. This is an easy fix. By adding `therubyracer` to the Gemfile, this will build a native extension. The build for the gem will add some time to the overall processing time of the pipeline.

Next issue, no Java. Codeship systems come pre-installed with Java so this step is all set, with Bitbucket Pipelines I needed to take care of this myself. Because they are using images from DockerHub, I was able to pull it down to my local system do some playing around with it. I found if I added `apt-get update` and `apt-get install --assume-yes openjdk-7-jre-headless` I was able to get s3_website working. Sadly this does add more time to the pipeline execution, as you need to wait for the system to update, and then install Java.

So, let's look at my `bitbucket-pipelines.yml`

{{< gist amscotti 07105c924a79927229ff7b0efab685ad "bitbucket-pipelines.yml" >}}

[https://gist.github.com/amscotti/07105c924a79927229ff7b0efab685ad](https://gist.github.com/amscotti/07105c924a79927229ff7b0efab685ad)

Overall it works, and I feel good about it, but I can make it better. With both of the changes I made, I have added time to the pipeline execution. I feel if I make an image with Java pre-installed this would cut down my build times. I’m able to do this because Bitbucket Pipelines can use any image from Docker Hub. Overall a great feature! So, my next steps are to build my own Docker Image to build my blog!
