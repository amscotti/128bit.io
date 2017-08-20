---
author: Anthony Scotti
date: 2010-10-02T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- API
- Howto
- ListManager
- Ruby
- SOAP
- XML
title: Ruby, HTTP Post and Lyris ListManager
url: /2010/10/02/ruby-http-post-and-lyris-listmanager/
---

A bit ago at work I was asked to help a customer with a solution for using the Lyris ListManager's SOAP API with just HTTP Post calls. They just needed to see some sample code that they could use to re-write. SOAP is XML based, you send and get back XML. Just using HTTP Post you need to format the XML you are sending and then parse out the information you get back from the SOAP server. Most languages have built in processes for dealing with SOAP based APIs, this makes life much easier and saves time from formatting the XML by hand. With using HTTP Post calls you need to have an understanding of the way that SOAP XML is laid out along with how the API is laid out by looking at the WSDL. Take a look at [SOAP from Wikipedia](http://en.wikipedia.org/wiki/SOAP) for more info on SOAP and how things are laid out.

Here's what I come up with!

{{< gist amscotti 5473854 >}}

The big thing is getting the SOAP Envelope formatted right, it takes some looking at the WSDL to figure out how to format the inputs data the right way but after a bit you can get the hang of it.

This example is obviously geared toward using ListManager, but can be applied to other SOAP based APIs.  

Open for questions, comments, or any way to improve this!
