Title: SQS, Amazon's Simple Queue Service with Node.js and Ruby
Date: 2012-06-03 00:00
Slug: 2012/06/03/sqs-amazons-simple-queue-service-with-node-js-and-ruby
Save_as: 2012/06/03/sqs-amazons-simple-queue-service-with-node-js-and-ruby/index.html
URL: 2012/06/03/sqs-amazons-simple-queue-service-with-node-js-and-ruby/
Tags: AWS, Howto, nodeJS, Queues, Ruby, SQS
Summary: Code examples demonstrating Amazon SQS queue operations in both Node.js and Ruby. Shows how to create queues, send messages, and receive messages using AWS SDKs in both languages, comparing API patterns and highlighting event-driven use cases for decoupling application components.

I've been really taking interest in the Amazon Web Services and trying to learn how to use them best I can. I really do find the Amazon Web Services a great set of tools that let you work with very scaleable services, but one thing you need to keep in mind is they are very "sticky". What I mean by sticky is once you fully integrate your applications into using them you are most likely not going to be switching any time soon. This really isn't that big of an issue as long as you are happy with them.

One of the things that can help build scaleable systems is the use of a queuing service, a very simple concept with huge advantages. More or less, with a queue system you are able to push messages on to a queue, the messages can represent work that needs to be done. You then can have a system on the backend receiving the messages and perform whatever tasks are needed along with removing the message from the queue. There are a good number of queuing service out there but like the other Amazon Web Services there is very little setup needed to use SQS.

Some terms and concepts before I show you the code, your Queue name is what you will see in the AWS console but this really relates to a URL. So if I have a Queue name of "test", the URL would look something like this https://queue.amazonaws.com/137023432286/test. This URL breaks down to https://queue.amazonaws.com/{accountid}/{queue_name}

When you send a message it will be put into the queue and listed under "Messages Available" in the AWS console. When a message is read from the queue it will move to "Messages in Flight" status which means it's not going to be read again the next time something reads the queue until the "Default Visibility Timeout" time has past. It will then be moved back to "Messages Available" status. The Default Visibility Timeout can be set when you make the queue, this is more or less the time it would take to process the job before is should be put back in to the queue for a retry.

One thing I feel that is important about using services is that they are cross-languages and cross-platforms. This will help keep you from being locked into a language or a specific platform, because you may find that something may work better down the line and being able to switch will be a big advantage. With this said, keep in mind that you maybe locked into using Amazon Web Services but at least you have some wiggle room as most languages have an API library for AWS.

So I have some small code examples one in node.js(in CoffeeScript) and the other in Ruby. The node.js sends a message on to the queue and the Ruby will read it from the queue and print it out to the console and remove it from the queue. Keep in mind that I'm sending JSON but I'm converting it to a string and then parsing it on the receiving side.

**Node.js Sender**

```coffeescript
aws = require ('aws-lib')

access_key_id = "<Your access key id>"
secret_access_key = "<Your secret access key>"

options = {
  "path" : "<Your queue URL, just the /accountid/queue_name is needed>"
}

sqs = aws.createSQSClient(access_key_id, secret_access_key, options)

outbound = {
  MessageBody : JSON.stringify({
    data: "Test Message",
    timestamp: new Date().getTime()
    })
}

sqs.call "SendMessage", outbound, (err, result) ->
  if err then console.log "SendMessage error: #{err}"
```

**Ruby Receiver**

```ruby
require 'rubygems'
require 'aws-sdk'
require 'json'

sqs = AWS::SQS.new(
    :access_key_id => '<Your access key id>',
    :secret_access_key => '<Your secret access key>')

url = "<Your queue URL>"

receive = sqs.queues[url].receive_message()
if receive
  puts JSON.parse(receive.body)
  receive.delete
end
```

It's a small example but if you see any improvements feel free to let me know or just fork the Gist.
