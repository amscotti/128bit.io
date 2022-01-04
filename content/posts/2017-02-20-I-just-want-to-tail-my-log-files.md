---
author: Anthony Scotti
date: 2017-02-20T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- RabbitMQ
- Logstash
- Elasticsearch
title: I just want to tail my log files!
url: /2017/02/20/I-just-want-to-tail-my-log-files/
---

I've had the opportunity to use the Elastic Stack (formally known as ELK) for some time now, there's a great number of use cases that the Elastic Stack can fit, but one of the primary uses is to help aggregate logs files into one centralized location. This gives you the ability to analyze and research your log files, at work we've been able to gain a lot more insight into our services using the Elastic Stack. For myself, it has been extremely exciting to work on this platform, scale it out, and ensure that it is meeting all our needs.

A few weeks ago I was chatting with a co-worker, he pointed out one area our Elastic Stack platform wasn’t great at, real-time streaming of logs. In other words, being able to tail a log file. Due to the nature of Elasticsearch, you will always have some kind of delay when getting results back. After listening to this I started thinking about what I could do to solve this need.

I know there are several different ways to solve this problem, and a lot of different tools that you could use to achieve the same results, for instance, one that I found while searching was [oklog](https://github.com/oklog/oklog). Because we already have the Elastic Stack in place, I wanted to use something that would fit into the tools we already had. I found a nice solution by being able to combined Logstash and RabbitMQ together to stream the logs to a user.

This works nicely because Logstash has a built-in [RabbitMQ Output Plugin](https://www.elastic.co/guide/en/logstash/current/plugins-outputs-rabbitmq.html) that can be used to send any event into RabbitMQ. Logstash will let you create an exchange, if you choose the exchange type of `topic` you will be able to filter the stream to only the logs you are interested in receiving by using a routing key. You also want to check that you have both `durable` and `persistent` set to **false**, this will ensure that no data is saved into RabbitMQ and overwhelm the system. In RabbitMQ, if there isn’t a queue linked to the exchange, the events will be dropped until someone creates a queue to view the stream. This will ensure that you don’t have data building up within your RabbitMQ system, and will only react when someone is interested in viewing the logs.


## How does this all work?
![Overview](https://d2mxuefqeaa7sj.cloudfront.net/s_C13745FF5716F8D4104CF125CEE4A4C893276FDC2E767C5421C419F90193F2AA_1487608735392_tail_logs_layout.png)


A lot of the code is just to simulate events coming from a log file, note that I am adding fields to the events. In this example, I am adding `environment` and `service`, these fields are going to be important because they are how we are going to filter the events downstream. Within the Logstash config, we are adding the fields to the key in the RabbitMQ output like so, `"logs.%{environment}.%{service}"`.

{{< gist amscotti a44b8e7d1da88711879d1c57b68da7b1 "rabbitmq_config" >}}

With this approach, you can make it as fine-grained as you want using any data available to Logstash to come up with a routing key for RabbitMQ. The key will really be based on your needs for the various services that you're running. If you're running multiple copies of the same services you may need to include the hostname or some other unique identifier to allow a way to filter log files per host. If you're gathering multiple log files from the same system, you may want to include the log file name as part of the key. You should really take some time to consider the end user experience and how they're going to filter down to get the information they need.


Consuming the stream is as simple as writing an application that will connect to RabbitMQ and create a queue on the exchange and bind the key to filter the logs by,


![logfile_output](https://d2mxuefqeaa7sj.cloudfront.net/s_C13745FF5716F8D4104CF125CEE4A4C893276FDC2E767C5421C419F90193F2AA_1487609219372_logs_output.png)


Here is an example of the program I quickly came up with to test this out, it is written in the Ruby language but picking something that your team is more familiar with could be more ideal. This should be a convenient tool they can use on demand. Overall you want the overhead of your teammates to be able to consume logs in this way to be as low as possible.

{{< gist amscotti a44b8e7d1da88711879d1c57b68da7b1 "read.rb" >}}

One interesting idea that I’ve been thinking about doing for a hackathon is building a simple web application that would connect to RabbitMQ and using WebSockets, would stream the desired log to the web browser. This would give people a quick and easy way to view logs without opening up a command prompt.

Now that my local testing is done I'm going to see if this can help my coworkers with their needs of real-time streaming of logs. I hope this helps other people that are tackling the same issue or at least help with devising some creative ways to solve this problem. If you know of any way to improve this or have noticed anything that could potentially go wrong, feel free to comment. I would love to hear any suggestions.
