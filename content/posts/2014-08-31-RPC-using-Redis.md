Title: RPC using Redis
Date: 2014-08-31 00:00
Slug: 2014/08/31/RPC-using-Redis
Save_as: 2014/08/31/RPC-using-Redis/index.html
URL: 2014/08/31/RPC-using-Redis/
Tags: RPC, Redis, Ruby, Python
Summary: Explores Remote Procedure Call as pattern for microservices architecture, comparing to message queues. Demonstrates JSON-RPC for message formatting with Redis pub/sub system for message distribution, showing how client waits for RPC return results while message queues typically trigger jobs without reply requirements.

One of the things I find myself always looking into and being excited about is scaling out systems. Now this means different things to different people. The reason for me looking into RPC is how to deal with [Microservices](http://martinfowler.com/articles/microservices.html) as part of a way to move Monolithic applications to into the Microservices architecture.

RPC [(or Remote procedure call)](http://en.wikipedia.org/wiki/Remote_procedure_call) is an idea that has been in computer science for a bit now. An over simplified way of thinking about is the ability to send a message to a remote process whether it is on the same system or remote. Overall this is very vague and is open to many implementations. In my mind, there are too many things in play when it comes to RPC, the format of the message and how you get the message to the remote process. There are many ways to do RPC and this is just my take on it but for this posting I am going to use '[JSON-RPC](http://en.wikipedia.org/wiki/JSON-RPC)' for the message formatting and Redis as the way of pushing messages around.

## RPC vs Message Queue
The ideas are mostly the the same but with RPC the client is waiting for a return message that has the results from the RPC call. If your Message Queue system allows you to address messages back to the sender then you can most likely use it for RPC. In most Message Queues, they are used to trigger jobs that are not needed to reply to the client.

## Why Redis and not something else?
You should be able to find Redis in most modern tech stacks somewhere, and if not, what's wrong with you? Redis is a great tool for many things and you should really look into it. With the idea of the path of least resistance and not needing to learn anything new, Redis fits into this perfectly, so let's see what we can do.

## Code

### Client
```ruby
require 'rubygems'
require 'redis'
require 'json'
require 'securerandom'

class Client
  attr_accessor :queue_name

  def initialize(queue_name)
    @queue_name = queue_name
    @redis = Redis.new
  end

  def method_missing(name, *args)
    call(name.to_s, args)
  end

  def call(method, params)
    jsonrpc_id = SecureRandom.uuid
    msg = {:jsonrpc => "2.0", :method => method, :params => params, :id => jsonrpc_id}.to_json
    @redis.rpush @queue_name, msg
    key, results = @redis.blpop jsonrpc_id
    JSON.parse(results)['result']
  end
end

rpc = Client.new "rpc"
puts rpc.echo "Hello World!"
puts rpc.add 10, 20
```

### Server
```ruby
require 'rubygems'
require 'redis'
require 'json'

class Server
  attr_accessor :queue_name

  def initialize(queue_name)
    @queue_name = queue_name
    @redis = Redis.new
  end

  def add(a, b)
    a + b
  end

  def echo(message)
    message
  end

  def listen
    loop do
      key, body = @redis.blpop @queue_name
      message = JSON.parse body
      if method = message['method']
        result = {:jsonrpc => "2.0", :result => self.send(method, *message['params']), :id => message['id']}.to_json
        @redis.rpush message['id'], result
      end
    end
  end
end

rpc = Server.new "rpc"
rpc.listen
```

So, this works due to Redis having commands to let you block as you wait for data to come back from the server. This is really nice as the client code looks like you are calling a local method.

## Ruby to Ruby is cool, but...
What if you want to use some other language? Well, as long as your language has good Redis library you should be able to do the same thing. Let's take a look at setting up a server in Python.

```python
import redis
import json

class Server:
    def __init__(self, queue_name):
        self.queue_name = queue_name
        self.r = redis.StrictRedis()

    def add(self, a, b):
        return a + b

    def echo(self, message):
        return message

    def listen(self):
        while True:
            key, body = self.r.blpop(self.queue_name)
            message = json.loads(body.decode())
            if "method" in message:
                result = json.dumps({"jsonrpc": "2.0", "result": getattr(self, message["method"])(*message["params"]), "id": message["id"]})
                self.r.rpush(message["id"], result)


rpc = Server("rpc")
rpc.listen()
```

## Conclusion
This is very much a proof of concept to test some ideas in my head,  definitely needs more work around handling exceptions. If you see any issues with this approach I would love you to reach out to me. I do hope to look into using [RabbitMQ](http://www.rabbitmq.com/) at some point for the same idea but this could be a great approach if you already have Redis in your stack.
