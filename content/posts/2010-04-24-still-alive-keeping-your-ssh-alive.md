Title: Still Alive: Keeping your SSH alive
Date: 2010-04-24 00:00
Slug: 2010/04/24/still-alive-keeping-your-ssh-alive
Save_as: 2010/04/24/still-alive-keeping-your-ssh-alive/index.html
URL: 2010/04/24/still-alive-keeping-your-ssh-alive/
Tags: Linux, SSH, Tip, UNIX
Summary: A quick tip for preventing SSH connections from dropping due to inactivity by editing the ssh_config file to send keep-alive packets every 30 seconds, ensuring stable connections on networks with aggressive timeout settings.

"This was a triumph."

If you find your SSH connections dropping or locking up after not being used for some time you may want to try to edit your `ssh_config` (/etc/ssh/ssh_config) file and uncomment/add in the line `ServerAliveInterval 30`. The number is in seconds.

What this will do is send a small 'keep-alive' packet to the server to ensure you don't get dropped.

Why is this happening? It could be settings on the server that drop users after set time of inactive use or due to a firewall/switch rule that drop inactive connections to improve the performance of the network.
