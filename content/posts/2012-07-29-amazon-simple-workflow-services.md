---
author: Anthony Scotti
date: 2012-07-29T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Amazon
- AWS
- Ruby
title: Amazon Simple Workflow Services
url: /2012/07/29/amazon-simple-workflow-services/
---

I’ve been researching [Amazon Simple Workflow Services](http://aws.amazon.com/swf/). This is a product which is like [Simple Queuing Services](http://aws.amazon.com/sqs/) but on steroids. It allows you to develop complex workflows that you’re able to scale out each part of the workflow as you need. There are a number of used cases on their site, one that managed to catch my eye is NASA. They are using Amazon Simple Workflow to process images captured by the Mars Exploration Rovers.

I originally looked into Amazon Simple Workflow sometime ago when it first came out. At the time I was very confused with their API and I didn’t feel that their documentation was complete. Looking into it again for a project at work with different eyes I was able to understand the API a bit more then last time. I still feel that the documentation is a bit lacking along with useful API calls missing. Because of this I feel that there is a steep learning curve and converting an app to use Simple Workflow would take some time.

After my research, I presented my findings to my teammates. I wanted to show them a demo that I could use to point out the different parts of the workflow. For my demo I made a [sandwich maker](https://github.com/amscotti/Simple_workflow_sandwich_maker), this code will allow you to build a sandwich from a web interface and deliver the order to the backend. At this point the decision part of the code which monitors the entire workflow will assign certain task to workers.

In my example I have one worker that can handle all the tasks, if I wanted to scale this out I could increase the number of workers and I would be able to process more tasks. If you wanted to fine-tune this example you could break the code from one worker into multiple workers for a precise task which would allow you to scale individual tasks. This dramatically allows you to scale your application needs and also allows you to configure your system the way you want it to be laid out.

Decision Code,

{{< gist amscotti 5400641 >}}

[Click here to view the full project on Github.](https://github.com/amscotti/Simple_workflow_sandwich_maker)

From the code you can see that I need to build two functions of my own. I first needed a function that will allow me to know what tasks have been completed along with the other function that will allow me to see the original input from the order.

Reference Links,

* [Amazon SWF Documentation](http://aws.amazon.com/documentation/swf/)

If you have any questions, comments, or ways to improve this code please feel free to post in the comments.