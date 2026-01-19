Title: Ruby, HTTP Post and Lyris ListManager
Date: 2010-10-02 00:00
Slug: 2010/10/02/ruby-http-post-and-lyris-listmanager/index.html
Save_as: 2010/10/02/ruby-http-post-and-lyris-listmanager/index.html
URL: 2010/10/02/ruby-http-post-and-lyris-listmanager/
Tags: API, Howto, ListManager, Ruby, SOAP, XML
Summary: A Ruby example demonstrating how to interact with Lyris ListManager's SOAP API using HTTP POST instead of built-in SOAP libraries. Shows how to manually construct the SOAP envelope XML, set proper headers including authentication, and parse the response for adding members to mailing lists.

A bit ago at work I was asked to help a customer with a solution for using the Lyris ListManager's SOAP API with just HTTP Post calls. They just needed to see some sample code that they could use to re-write. SOAP is XML based, you send and get back XML. Just using HTTP Post you need to format the XML you are sending and then parse out the information you get back from the SOAP server. Most languages have built in processes for dealing with SOAP based APIs, this makes life much easier and saves time from formatting the XML by hand. With using HTTP Post calls you need to have an understanding of the way that SOAP XML is laid out along with how the API is laid out by looking at the WSDL. Take a look at [SOAP from Wikipedia](http://en.wikipedia.org/wiki/SOAP) for more info on SOAP and how things are laid out.

Here's what I come up with!

```ruby
require 'net/http'
require 'net/https'
require 'base64'

http = Net::HTTP.new('go.netatlantic.com', 82)
http.use_ssl = false
path = '/'

# SOAP Envelope
data = <<-EOF
<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope
xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:ns1="http://tempuri.org/ns1.xsd"
xmlns:ns="http://www.lyris.com/lmapi">
<SOAP-ENV:Body>
<ns:CreateSingleMember>
<EmailAddress xsi:type="xsd:string">amscotti@128bitstudios.com</EmailAddress>
<FullName xsi:type="xsd:string">Anthony Scotti</FullName>
<ListName xsi:type="xsd:string">mylistname</ListName>
</ns:CreateSingleMember>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>
EOF

# Set Headers
headers = {
  'Referer' => 'http://www.128bitstudios.com/',
  'Content-Type' => 'text/xml',
  'Host' => 'go.netatlantic.com',
  'Authorization' => 'Basic ' + Base64::encode64("amscotti@128bitstudios.com:password")
}

# Post the request
resp, data = http.post(path, data, headers)

# Output
puts 'Code = ' + resp.code
puts 'Message = ' + resp.message
resp.each { |key, val| puts key + ' = ' + val }
puts data
```

The big thing is getting the SOAP Envelope formatted right, it takes some looking at the WSDL to figure out how to format the inputs data the right way but after a bit you can get the hang of it.

This example is obviously geared toward using ListManager, but can be applied to other SOAP based APIs.

Open for questions, comments, or any way to improve this!
