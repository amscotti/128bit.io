Title: Stopping SSH Brute Force attacks on Linux
Date: 2010-08-30 00:00
Slug: 2010/08/30/stopping-ssh-brute-force-attacks-on-linux
Save_as: 2010/08/30/stopping-ssh-brute-force-attacks-on-linux/index.html
URL: 2010/08/30/stopping-ssh-brute-force-attacks-on-linux/
Tags: DenyHosts, Fedora, Howto, iptables, Linux, SSH
Summary: A guide to protecting SSH servers on Linux from brute force attacks. Covers disabling root login, changing SSH ports, using iptables rate limiting rules to temporarily block aggressive IPs, and installing DenyHosts for permanent blocking with optional synchronization to a community blocklist.

From my other posting "[Stopping SSH Brute Force attacks with PF on FreeBSD](/2010/06/13/stopping-ssh-brute-force-attacks-with-pf-on-freebsd/)" I've been getting a good number of hits from people searching on how to stop SSH Brute Force attacks but on Linux and not FreeBSD, so I kind of feel the need to make a posting on this for the linux people. I also just setup a Fedora 13 server on Rackspace's Cloud and I wanted to ensure I could stop SSH Brute Force attacks.

## Quick over view from my other posting

You should make sure that no one can log in as root from SSH. A lot of servers let you do this so you can get things setup. So make a new user, install sudo and add them do the sudoers list. After that edit your /etc/ssh/sshd_config file to have ‘PermitRootLogin’ set to ‘no’. Don't forget to restart sshd for the new setting to take place `service sshd restart` on Fedora. This set is key as root is the only known user on all Linux/Unix base system.

A lot of SSH Brute Forcers are only looking at port 22 for SSH, you can change the port that SSH is running and stop a lot of SSH Brute Force attacks. This can be done within /etc/ssh/sshd_config or by using your firewall. I'm really not a big fan of this step but it helps out a lot.

## iptables - Linux Firewall

iptables is the linux firewall that comes pre-installed on a lot of distros. Within Fedora it comes pre-installed and is able to run  from first boot. Looking around on the web I couldn't find anything on the same level as what I had for PF but I did find something that would help slow down SSH Brute Force attacks.

The file that keeps all the rules for iptables can be found in /etc/sysconfig/iptables on Fedora, add the lines below to the file.
```
-I INPUT  -p tcp -m tcp --dport 22 -m state --state NEW -m recent --set --name SSH--rsource
-I INPUT -p tcp -m tcp --dport 22 -m state --state NEW -m recent --update --seconds 180 --hitcount 4 --name SSH--rsource -j DROP
```
The first rule will start a table that will log IPs which starts a connection to ssh port. The next rule will count the number of tries from the same IP, if that count passes 4 with in 180  seconds then the server will not accept any more connections from that IP for 180 seconds.

You are going to need to restart iptables, this can be done on Fedora by running `service iptables restart`.

The idea with this rule is that the SSH Brute Forcer is just a script that is running until it see that it's being blocked and move on to the next IP.

## DenyHosts

After looking around for software that would give me something more permanent for blocking SSH Brute Force attackers I found DenyHosts.

From [denyhosts.sourceforge.net](http://denyhosts.sourceforge.net/),

> "DenyHosts is a script intended to be run by Linux system administrators to help thwart SSH server attacks (also known as dictionary based attacks and brute force attacks)."

DenyHost will read you log file looking for fails from SSH connections, it will then add that IP to your /ect/hosts.deny and block them from being able to log in at all. You can also set it to deny the IP from all services on the server.

I found DenyHosts to be easy to install and setup. On Fedora to install it is just using `yum install denyhosts`, to run is `service denyhosts start` start and to have it run on boot `chkconfig denyhosts on`

One of the things DenyHosts does that takes it a step beyond the rest, is it lets you sync up with their network of other people submitting IPs of SSH brute forcers. So you will be blocking attacks before they even start, which is really nice!

I highly recommend using DenyHosts, it's great software that really give you sound of mind about SSH Brute Force attacks. DenyHosts will run on other OS beside Linux like FreeBSD, Max OS X and Solaris.

Would love to hear other ideas or software people are using to help block SSH Brute Force attacks.
