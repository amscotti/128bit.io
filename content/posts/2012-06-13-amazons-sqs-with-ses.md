---
author: Anthony Scotti
date: 2012-06-13T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Amazon
- Howto
- nodeJS
- Ruby
- SES
- SQS
title: Amazon's SQS with SES
url: /2012/06/13/amazons-sqs-with-ses/
---

Keeping with learning more about Amazon Web Services, I wanted to build on the examples I did for SQS along with using Amazon Simple Email Service. The [Simple Email Service](http://aws.amazon.com/ses/) is, as you could guess, for sending emails. It gives you sending features of a large [Email Services Provider](http://en.wikipedia.org/wiki/E-mail_service_provider) but with a low entry point. Just like lot of the other Amazon services, you pay for what you use without any contracts. Simple Email Service is something that you do need to request full access to the service before you can just use it, until you do this you are sandboxed and can only send to email addresses that you have verified. I see Simple Email Service used more for transactional based emails (like user registrations or passwords resets) then marketing type emails but there is no limitations on how you use the service. You do get access to Deliveries, Bounces, Complaints and Rejected statistical data. You can use this data to solve compliance issues.

The API to use SES is very easy, most of the API calls are to deal with quotas and your statistics, because sending an email is easy.

Using the code from my last post with some updates,

**Node.js Sender**

{{< gist amscotti 2927657 "node_send.coffee" >}}

**Ruby Receiver**

{{< gist amscotti 2927657 "ruby_receive.rb" >}}

You now see the Ruby code is in a "while loop", that will keep on looking at the queue for new messages. If a new message is sent, it will the send out an email based on the data from the message. Even though this is very simple, the idea is great. By pushing the task of sending the e-mail, it makes the center code run faster without the need of sending the e-mail itself. If this code was part of a web request, you are now able to return a message to the user sooner rather than having an e-mail sent and then responding. Overall this makes your application more responsive. Now imagine this is a task that is the main focus of your application that takes some time and CPU to complete. You are able to look at the size of your queue and start up additional workers to help get through the backlog of work. This can be done by Auto-scaling on EC2 or adding additional worker nodes if you are using Heroku. You now have a very linear way of processing work faster when needed. The key idea is "when needed" because when the queue is low, you are able to drop workers that you no longer need and reduce your cost. I feel strongly that this idea is a huge benefit for using cloud based infrastructures.

One draw back I found of SES is (unless I over looked this in the API documentation) there is no way to send batch mailings using the API, you must send one email at a time. Also by using SES there are many thins that Amazon pushes off on to you like list management and templating. Most email service providers will have in their software, ways of making easy to use templates and dealing with list management, just keep in mind that you will need to roll your own solutions.

Here are some resources links,
*  [Auto-scaling Amazon EC2 with Amazon SQS](http://aws.amazon.com/articles/1464)
*  [Simple Queue Service FAQs](http://aws.amazon.com/sqs/faqs/)
*  [Simple Email Service FAQs](http://aws.amazon.com/ses/faqs/)

If you see any improvements feel free to let me know or [just fork the Gist](https://gist.github.com/2927657).