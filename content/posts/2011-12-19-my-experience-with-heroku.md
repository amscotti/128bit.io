Title: My experience with Heroku
Date: 2011-12-19 00:00
Slug: 2011/12/19/my-experience-with-heroku
Save_as: 2011/12/19/my-experience-with-heroku/index.html
URL: 2011/12/19/my-experience-with-heroku/
Tags: Heroku, Opinion, Platform as a Service, Ruby
Summary: Review of Heroku as Platform as a Service solution for developers who want to focus on code rather than server management. Offers free web node for testing, easy scaling with commands, extensive add-ons for databases and monitoring, clean documentation, and Git workflow deployment. Personal site amscotti.com currently hosted successfully on Heroku.

I haven't done too much publishing of web applications for my own stuff. At work we have an Ops team that deals with setup and deployment of our code. I have used Rackspace cloud and AWS for setting up servers before but mostly just for testing and nothing for production. As a developer I want to focus on the code and not fine tune an application server. I want to be able to write code, push it out and scale without putting much thought in to it. Oh, and I want do to do this without hiring a Ops team of my own! :P

![Heroku Logo](/images/logo/heroku-logo_big-300x93.png)

Platform as a Service (or PaaS) is what I'm looking for. There are sites like [Engine Yard](http://www.engineyard.com), [DotCloud](https://www.dotcloud.com/) and many others that give developers what I'm looking for, the ability to just focus on writing great code and not to worry about hosting your application. I have been reading a lot about [Heroku](http://www.heroku.com/), they started as just a Ruby and Ruby on Rails hosting but now are able to host applications made in Python, Node.js, Java, Scala, and Clojure along with Ruby. To me this makes Heroku a one stop shop for hosting. Heroku will give you one free web node to get you up and running. This is a great way to test your application and see how to runs on their system without it costing you anything. Scaling up is as easy as running a command to add more web nodes or workers to your application. They also allow you to scale down to save money when traffic is low.

Heroku also has a large number of 'add-on' for things from, MongoDB hosting to add-on that allow you to monitor and tuning your application. All the add-ons are fully documented and give you clear examples on how to use them. Speaking of documentation, I do have to say that the layout of the documentation on the Heroku site is great and I was able to quickly find anything I needed to know.

Like others in the space Heroku uses the Git workflow. After getting things all set (which didn't take long at all), you just need to do a 'git push heroku master' to push out to Heroku and they will take care of the rest for you (restarting, installing gems, updating files and starting the app again.... you know, all the fun stuff!). If you are already using Git for your version control system then this will feel very natural to you.

Right now [amscotti.com](http://amscotti.com/), my personal site, is being hosted on Heroku for free as it's a low traffic site without need for more then just one web node. With my experience with Heroku so far I can safely say that the next web app I push out will be on Heroku and I would highly recommend to anyone looking for a easy way to host your web apps.

Anything you want to share about Heroku? Good or bad is welcome. Any other Platform as a Service that is worth a look? Post in the comments!
