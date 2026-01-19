Title: Yeoman working with APIs
Date: 2013-06-01 00:00
Slug: 2013/06/01/yeoman-working-with-apis
Save_as: 2013/06/01/yeoman-working-with-apis/index.html
URL: 2013/06/01/yeoman-working-with-apis/
Tags: Yeoman, APIs, NodeJS
Summary: Solution for Yeoman CORS issue when APIs run on different domains. Creates Node.js proxy server with Connect and http-proxy to route Yeoman app API requests to local development API server, preserving live preview and avoiding cross-origin restrictions.

From my [last post](/2013/05/28/my-friend-yeoman/), I talked about how great Yeoman is. I have found one issue with Yeoman but there is a easy solution. Yeoman comes with its own built-in server which is very convenient, but if you're working on a application which requires access to an API this becomes an issue due to cross site domain.

For some time I've been making a symbolic link of my Yeoman app folder into my Tomcat's webapp folder which would allow me to access the API running on the same server. Since I am both a back-end and front-end developer, having the set up is not too much of an issue for me. Thinking from a point of view as someone new working on just the front-end of this project, the setup needed is kind of a pain due to a requirement of having the full stack running on your local system.

My solution to this was to setup a local server that could proxy calls to the API. I made a small Node.js server that uses [Connect](http://www.senchalabs.org/connect/) and [http-proxy](https://github.com/nodejitsu/node-http-proxy).

Here is the code,

```javascript
var httpProxy = require('http-proxy'),
  staticDir = 'app',
  apiHost = '<Your API Host>',
  apiPort = 80,
  apiPath = '/api';

var proxy = new httpProxy.RoutingProxy();
connect()
  .use(connect.logger("dev"))
  .use(function (req, res, next) {
    if (req.url.indexOf(apiPath) === 0) {
      proxy.proxyRequest(req, res, {
        host: apiHost,
        port: apiPort
      });
    } else {
      next();
    }
  })
  .use(connect.static(staticDir))
  .listen(process.env.PORT || 8000);

console.log("Loading Server at http://localhost:" + (process.env.PORT || 8000));
```

To setup the dependencies in your package.json file add in this,
```
   "http-proxy": "0.8.x",
   "connect": "2.3.x"
```
Then run `npm install` to install them.

If you want to take this one step farther, you can also add this to your package.json
```
 "scripts": {
    "start": "node server.js"
  }
```
This will add a command to npm that will let you now run `npm start` and it will load the server for you.

This cuts down the over head of what I need to run just to work on the front-end code and lets other developers on the team quickly work on the project too. I hope this helps anyone working with Yeoman on apps that need to talk to a API.
