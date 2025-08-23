Title: Setting up a Riak Cluster
Date: 2013-05-08 00:00
Slug: 2013/05/08/setting-up-a-riak-cluster
Save_as: 2013/05/08/setting-up-a-riak-cluster/index.html
URL: 2013/05/08/setting-up-a-riak-cluster/
Tags: Riak, Cluster, noSQL
Summary: Comprehensive guide to setting up Riak distributed database cluster on Amazon EC2 with Ubuntu. Covers installation with Homebrew, security group configuration for Erlang ports, system setup steps, firewall configuration for cluster communication ports, node configuration, and clustering best practices.

![Riak Logo](/images/logo/Riak_logo.png)

Riak is a database that I have read a good amount about but have not actually gone through fully taking the time to investigate it. (AKA playing with it!)

## What is Riak

Riak is dynamo inspired database that is based off of Amazon's white paper. As with a lot of NoSQL databases it's easy to scale and it is fault-tolerant. Riak comes with a HTTP interface along with a Protocol Buffers interface. You can even use Riak to host HTML/JS applications like with [CouchDB's CouchApps](http://couchapp.org/page/index). It's also written in Erlang, so you know it's going to be good!

## Installing

It's easy enough to install Riak on a Mac by using Homebrew. Just type `brew install riak` and then you are good to go. But what about setting up a cluster? Like most NoSQL databases Riak expects to be run in a cluster, luckily Riak is supposed to be easy to set up in a cluster. Let's take a look to see if this is true!

### Setting up a cluster

I'm going to be setting up my cluster on Amazon using Ubuntu EC2 images. If you wish to use another distribution of Linux you should be able to find installation instructions on Basho's website.

### Firewall

The very first thing that you need to do is set up your firewall, in Amazon's case this is a security group.

![Riak Firewall Settings](/images/setting-up-a-riak-cluster/riak_firewall.png)

The systems in the cluster need to be able to communicate on certain ports, and reading [Basho's firewall configurations page](http://docs.basho.com/riak/latest/cookbooks/Network-Security-and-Firewall-Configurations/) here are the ports: 4369, 8099, and 6000-7999. This range is set up by you and can change. You'll see where the settings are for this when we install Riak.

You also need ports open so a Riak client can connect to the systems. The ports are 8098, and 8087. You should also have port 22 open so you can SSH into the system to do the install.

### Start up the servers

Ideally, you would want 3+ nodes in a Riak cluster. Easily enough to do in Amazons EC2. If you use the 'Classic Wizard' you can type into 'Number of Instances' 3. If you are using 'Quick Launch Wizard' to do this, just remember to hit edit details button and pick the right security group before launching the new instance.

![Riak Systems](/images/setting-up-a-riak-cluster/riak_systems.png)

If you are also using Ubuntu, you should pick the LTS (as of right now it's, 12.04.1) because that seems to be the one that Basho has tested against.

After the systems are fully up and running, SSH into the systems and start the install of Riak.

Basho has a great write up on how to install onto a Debian/Ubuntu system that you can follow here, [Installing on Debian and Ubuntu](http://docs.basho.com/riak/latest/tutorials/installation/Installing-on-Debian-and-Ubuntu/).

After installing Riak on all the nodes, you need to update the /etc/riak/vm.args. This will let you change the name of the node. Change it to riak@"IP of the system". You can find the IP by doing `ifconfig` at the command line or looking at the EC2 instance's Private IPs.

Next you're going to want to update the /etc/riak/app.config file,

Add this to the top of the file, this will limit the range of ports for the Erlang interpreter.
```
{ kernel, [
            {inet_dist_listen_min, 6000},
            {inet_dist_listen_max, 7999}
          ]},
```

The next lines will tell Riak what network interface and port to run on. Change this to the IP of your system.

```
{pb_ip, "127.0.0.1" },` to `{pb_ip, "IP of the system" },
```

```
{http, [{ "127.0.01", 8098 }]},` to `{http, [ {"IP of the system", 8098 } ]},
```

### Joining the cluster

After each node is fully named and configured, start up riak by running `riak start` on all the nodes. When riak is all set and loaded, pick an IP of one of the nodes and run `riak-admin cluster join riak@'IP node'` on the other two nodes.

This will add the nodes in a staging area, run `riak-admin cluster plan` to see the list of nodes in the staging area. To except the default plan, run `riak-admin cluster commit`.

At this point you should have a cluster up and running, let's give it a test!

### Testing the cluster

Let's put some data into the Riak database and see if we can get it back. We can use curl from the command line, find the Public DNS for one of the nodes and run this command.

```
curl -X PUT http://Public DNS:8098/riak/test/doc -H "Content-Type: application/json" -d '{"foo":"bar"}'
```

This will put the data into the Riak database, now let's see if we can get it back by running another curl command,

```
curl http://Public DNS:8098/riak/test/doc
```

You should see, {"foo":"bar"}, so far so good; now lets try and ask another node in the cluster for the same thing. Using another node's Public DNS run the same curl command like so,

```
curl http://Public DNS:8098/riak/test/doc
```

and you should see the same `{"foo":"bar"}`!

![Riak Test](/images/setting-up-a-riak-cluster/riak_test.png)

### Load balancing

Now for the final part, using Amazon we can easily set up a Load-balancer for our nodes. This will ensure that traffic is distributed evenly over the cluster. This is optional because the Riak clients are able to connect to a list of nodes to perform their own load balancing, but I feel there are more options using a load balancer from Amazon.

![Riak Load Balancer](/images/setting-up-a-riak-cluster/riak_loadbalancer.png)

Simply create a new load balancer and add the following,

* 8098 (HTTP) forwarding to 8098 (HTTP)
* 8087 (TCP) forwarding to 8087 (TCP)

Set the Ping Path to just / on port 8098

The load balancer will take a bit to start up, wait for the console to update the status to say that all the nodes are in service. After that, run the same steps as before to test the load balancer but using the DNS name from the load balancer.

## Done?
At this point the clusters are up and running and have a load balancer in front of it. Depending on the size of the systems and how much to disk space they have, I would say this is a pretty good **start**. There are more options Riak has to help fit how you're planning on using the database. I'm hoping this will give you a quick overview of how easy it is to set up the cluster and add notes as you need them, but you should definitely do more research if you are planning on using this in production.

## Side note
If you started the Riak Service before fully configuring the name, you may not be able to start Riak up.

You should be able to run `riak-admin cluster replace riak@127.0.0.1 riak@'ip of the system'` to fix this.

Another setup would be to run `rm -rf /var/lib/riak/ring/*` from the posting on [Stack Overflow](http://stackoverflow.com/questions/13859906/riak-node-no-longer-working-after-changing-ip-address)

## Other Riak Resources
* [Basho's Riak's homepage](http://basho.com/riak/)
* [How 3 Companies Are Using NoSQL Database Riak](http://readwrite.com/2011/02/09/how-3-companies-are-using-nosq)
* [Justin Sheehy on Riak & Distributed Systems](http://nosqltapes.com/video/justin-sheehy-on-riak-distributed-systems)
* [My Year of Riak](http://inaka.net/blog/2011/08/25/when-to-use-riak/)
* [Why I Think Riak is a Great NoSQL Option](http://architects.dzone.com/articles/why-i-think-riak-great-nosql)
* [myNoSQL's Riak News](http://nosql.mypopescu.com/tagged/riak)
* [Riak Handbook](http://riakhandbook.com/)
