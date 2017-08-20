---
author: Anthony Scotti
date: 2011-11-25T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Howto
- LinkedIn
- Ruby
- Sinatra
title: LinkedIn authentication with Sinatra
url: /2011/11/25/linkedin-authentication-with-sinatra/
---

To take the [authentication with Sinatra](http://www.128bitstudios.com/2011/11/21/authentication-with-sinatra) a bit farther you may want to use  another service to do your authentication against. This is some sample code adapted from a [Rails example](http://pivotallabs.com/users/will/blog/articles/1096-linkedin-gem-for-a-web-app). This code takes use of the [linkedin gem](https://github.com/pengwynn/linkedin) from [Wynn Netherland](http://wynnnetherland.com/) to do the authentication and also make some calls to the LinkedIn API. There are other gems that just do authentication for many services like Facebook and Twitter but for this sample I wanted to be able to make additional calls to the LinkedIn API.

{{< gist amscotti 1395030 >}}

If you know of any way to make this code better please comment or fork the Gist.
