Title: Sinatra with WebSockets
Date: 2012-04-16 00:00
Slug: 2012/04/16/sinatra-with-websockets
Save_as: 2012/04/16/sinatra-with-websockets/index.html
URL: 2012/04/16/sinatra-with-websockets/
Tags: Howto, Ruby, Sinatra, WebSockets
Summary: An example of adding WebSocket support to Sinatra applications using em-websocket gem. Shows how to start WebSocket server alongside Sinatra, handle connections and messages for real-time bidirectional communication, enabling features like live chat or real-time updates in Sinatra apps.

[WebSockets](http://en.wikipedia.org/wiki/WebSocket) are a hot topic now a days with the HTML5 push, even though they are not officially part of HTML5 spec. If WebSockets are new to you, they are a way of being able to keep a connection open from the client's browser to the server. It will let you push data back and forth, think AJAX but without  the need of pulling for new data over and over. WebSockets give you the ability to push, which gives you a very close to real time update on the client's side. At this time, most of the newest versions of the popular browsers support WebSockets.

Due to the real time factor of WebSockets, they have found themselves into online games. One of my new favorite examples of this is [http://browserquest.mozilla.org/](http://browserquest.mozilla.org/), a multiplayer Zelda clone. You see a lot of examples using [Node.js](http://nodejs.org/) along with [Socket.IO](http://socket.io/), which is a great pack of new technologies [example of my own](/2011/06/29/a-look-in-to-nodejs/)) but what if  you don't feel like switching to a new platform to take use of WebSockets? Most languages have libraries for dealing with WebSockets. In Ruby there is an em-websocket gem which is an EventMachine based WebSocket server.

I have a small project on GitHub which shows how I setup a Sinatra application to take uses of WebSockets to make a chat application. Nothing too great but this should give you an idea of where to start.

Here is the main part of the code,

```ruby
require 'rubygems'
require 'em-websocket'
require 'yajl'
require 'haml'
require 'sinatra/base'
require 'thin'

EventMachine.run do
  class App < Sinatra::Base
      get '/' do
          haml :index
      end
  end

  @channel = EM::Channel.new

  EventMachine::WebSocket.start(:host => '0.0.0.0', :port => 8080) do |ws|
      ws.onopen {
        sid = @channel.subscribe { |msg| ws.send msg }
        @channel.push "#{sid} connected!"

        ws.onmessage { |msg|
          @channel.push "<#{sid}>: #{msg}"
        }

        ws.onclose {
          @channel.unsubscribe(sid)
        }
      }

  end

  App.run!({:port => 3000})
end
```

Link to the full project [here on Github](https://github.com/amscotti/em_sinatra_chat), if you have any questions or comments please post, also any suggestions on improving this are welcome.
