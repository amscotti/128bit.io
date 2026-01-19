Title: Docker and Dokku, My Weekend Discovery
Date: 2013-06-23 00:00
Slug: 2013/06/23/docker-and-dokku-my-weekend-discovery
Save_as: 2013/06/23/docker-and-dokku-my-weekend-discovery/index.html
URL: 2013/06/23/docker-and-dokku-my-weekend-discovery/
Tags: Docker, Dokku, Linux, Virtualization, Heroku, PaaS
Summary: An introduction to Docker for operating system-level virtualization with minimal overhead compared to hypervisors. Covers creating containers for application components like databases and web servers, security benefits of isolation, and discovering Dokku for PaaS-like deployment similar to Heroku.

I'm primarily a Software Developer but I still have a great passion for System Administration. I work with Linux based systems now but if you look at some of my older postings you will find that I have done some work on [FreeBSD](http://www.freebsd.org) and [OpenSolaris](https://en.wikipedia.org/wiki/OpenSolaris). One of the things that really drove me to FreeBSD and OpenSolaris was their idea of [Operating system-level virtualization](http://en.wikipedia.org/wiki/Operating_system-level_virtualization), [FreeBSD with Jails](http://en.wikipedia.org/wiki/FreeBSD_jail) and [OpenSolaris with Zones](http://en.wikipedia.org/wiki/Solaris_Containers). By using these ideas of containers to isolate components of an application you could develop some really interesting ideas for laying out an application securely and effectively.

## Operating system-level virtualization

Operating system-level virtualization has an advantage over hypervisor virtualization due to having little or no overhead. This means there are more resources allocated to the system to run additional services than to run the actual hypervisor.

There are many interesting things that you can do with system-level virtualization, you can securely isolate components of an application. For example the database, web server, and any additional aspects of the application could all be isolated into their own containers. From a security standpoint, this means that one aspect of your application will not compromise the rest.

You could also segment resources on a machines to produce something similar to Amazon EC2 or Rackspace's Cloud which is in fact what [Joyent](http://joyent.com) is doing on top of [SmartOS](http://smartos.org/) (a fork of OpenSolaris). Joyent is making good use of Solaris' Zones which are capable of running the KVM hypervisor, this gives an additional level of virtualization to run non-solaris system within a Solaris Zone. This is some amazing use of containers.

## So, what about Linux?

As far as I know (and I could be wrong) there wasn't anything that was on the same level as Jails or Zones. Linux had [Chroot](https://en.wikipedia.org/wiki/Chroot) which is used to isolate processes and limits its exposure to the rest of the system. Typically you would find people running Apache in a Chroot for additional security. When I was looking at this, Chroot didn't possess the same capabilities as Jails or Zones. I know there are some projects that were used to expand out Chroot capability, like LXC but I've not seen much talk about this until now.

## Here comes Docker to the rescue!

[Docker](http://www.docker.io) is a project out of [dotCloud](https://www.dotcloud.com) which brings the idea of containers to Linux in an equivalent capability of Jails and Zones. From my understanding, Docker is part of dotCloud's infrastructure that they have decided to open source. I really enjoy when a company is willing to open part of their infrastructure to the public. It not only helps the community but it also helps the company.

Docker makes it easy to run and manage containers, giving a way to deploy applications in a highly portable fashion. Docker has the capability of creating images from your containers and sharing them across systems or online. Docker is very feature-rich and has a growing community that is contributing to the Docker project and also creating images that you can simply download and run.

## Dokku, one step farther!

Dokku is really where it started for me this weekend, it was shared with me as a tweet from my friend [Simon](http://newtriks.com/) talking about setting up your own mini-Heroku. The Dokku takes heavy use of Docker to setup containers for your applications along with some other open projects and a lot of great ingenuity from [Jeff Lindsay](https://twitter.com/progrium) and others.

I really can't say anything that isn't in the video by Jeff Lindsay beside saying, yes… it's that easy to set up.

<div class="video-embed">
<iframe src="https://player.vimeo.com/video/68631325" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>
</div>

[Dokku: Your own mini-Heroku in under 5 minutes](http://vimeo.com/68631325) from [Jeff Lindsay](http://vimeo.com/progrium) on [Vimeo](http://vimeo.com).

I see Dokku being used in many ways for example, set this up on your local system to deploy applications for testing, or on a public cloud to have similar functionalities to Heroku. Using Dokku on your own systems will allow you to have more control over the size of systems you want to use.

## Sadly the weekend is over

Both Docker and Dokku are excellent projects, that one weekend is not nearly enough time to fully appreciate them. I'm hoping to spend some more time working on better learning Docker and playing around more with Dokku. In time hopefully will even committing some of my own images for services to Docker. I'll be keeping an eye on both of these projects because I expect good things to come from them.

I also applaud dotCloud for open sourcing part of their infrastructure. This is a type of action from a company that really impresses me and makes me want to support them.

## Additional Resources
* [Docker Home Page](http://www.docker.io/)
* [The future of Linux Containers by Solomon Hykes](http://www.youtube.com/watch?v=9xciauwbsuo)
* [Docker: Linux Containers Made Easy](http://www.youtube.com/watch?v=fSQoDISuUec) - Starts at about 49:10
* [Dokku: The smallest PaaS implementation you've ever seen](http://progrium.com/blog/2013/06/19/dokku-the-smallest-paas-implementation-youve-ever-seen/)
* [Building Your Own Platform Service Using Docker](http://vimeo.com/67284401)
