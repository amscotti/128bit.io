Title: Stopping SSH Brute Force attacks with PF on FreeBSD
Date: 2010-06-13 00:00
Slug: 2010/06/13/stopping-ssh-brute-force-attacks-with-pf-on-freebsd
Save_as: 2010/06/13/stopping-ssh-brute-force-attacks-with-pf-on-freebsd/index.html
URL: 2010/06/13/stopping-ssh-brute-force-attacks-with-pf-on-freebsd/
Tags: FreeBSD, Howto, PF, SSH
Summary: A comprehensive guide to using the PF firewall on FreeBSD to block SSH brute force attacks. Covers enabling PF, creating a brute force table with tracking rules, and using pfctl commands to manage blocked IPs, providing automated protection against password guessing attempts.

Most people know that port 22 is used for SSH communication and due to this common knowledge, you get people using scripts to test for weak passwords. If you look into your /var/log/auth.log and you see tons of fails/errors from users not on your system or from invalid passwords for root, it means you have people trying to break into your system. Truthfully, anyone that puts a system online with port 22 open will see this happen to them. It's quite common and not direct attack against you, just scripts looking for IPs with port 22 open.

Now it goes without saying that you should make sure you have a strong password that take use of numbers, upper and lower case letters and symbols. Doing this will go along way in preventing someone from breaking into your system. You should also ensure that people can't remotely log in as root by setting 'PermitRootLogin' to 'no' in your /etc/ssh/sshd_config file. This will ensure that no matter how many passwords they try for root they will never be able to log in. One think that is better then just having passwords is setting up SSH keys, take a look at this posting [Making and using SSH Keys](/2010/04/10/making-and-using-ssh-keys/)

Now you could just set your SSH server to run on a different port or have your firewall redirect a different port from the outside to the system, but what's the fun in that when you can use a great tool like PF.

[PF or Packet Filter](http://openbsd.org/faq/pf/) comes from the OpenBSD group and was ported over to FreeBSD. It's a great firewall tool with many advanced features to it. PF comes pre-installed and just needs a quick edit to your /etc/rc.conf. Just add the lines below.

```
pf_enable="YES"
pf_rules="/etc/pf.conf"
pflog_enable="YES"
```

Now we need to add some rules to the /etc/pf.conf file that will deal with the SSH brute force attacks.
```
table <bruteforce> persist
block quick from <bruteforce>

pass inet proto tcp from any to any port ssh
flags S/SA keep state
(max-src-conn 5, max-src-conn-rate 5/30,
overload <bruteforce> flush global)
```

What is happening here is that you are making a table that will keep track of the IPs of SSH brute forcers and make sure they are unable to connect to the system after being added to the table. The next part in the rule is how they are added to the table. If they connect with more then 5 clients to the SSH server and try reconnect 5 times within 30 secs they get added to the table. Feel free to edit the rules for whatever works best for your situation. For myself, this works fine and deals with anyone quickly.

If you want to see the IPs on the table you can run `pfctl -t bruteforce -T show` as root and get a list. If somehow an IP gets put in the table that you don't wanted blocked you can removed it by running `pfctl -t bruteforce -T delete <IP>` and that will remove it from the table.

For people using Linux, I believe there are ways to do the same thing with something called [iptable](http://en.wikipedia.org/wiki/Iptables). If I ever set this up I will make a posting on it.

**EDIT**: I made a new posting going over ways to stop SSH brute force attacks on Linux. The posting can be found here, [Stopping SSH Brute Force attacks on Linux](/2010/08/30/stopping-ssh-brute-force-attacks-on-linux/)

Open for questions, comments, or any way to improve this!
