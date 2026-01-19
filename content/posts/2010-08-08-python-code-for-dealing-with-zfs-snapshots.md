Title: Python code for dealing with ZFS snapshots
Date: 2010-08-08 00:00
Slug: 2010/08/08/python-code-for-dealing-with-zfs-snapshots
Save_as: 2010/08/08/python-code-for-dealing-with-zfs-snapshots/index.html
URL: 2010/08/08/python-code-for-dealing-with-zfs-snapshots/
Tags: FreeBSD, Howto, Opensolaris, Python, Solaris, ZFS
Summary: Two Python scripts for managing ZFS snapshots. The first script creates timestamped snapshots of all filesystems in a zpool. The second script automatically removes snapshots older than 30 days by parsing the timestamp in snapshot names, useful for automated backup cleanup.

From my last posting about ZFS "[Fun with ZFS send and receive](/2010/07/23/fun-with-zfs-send-and-receive/)" we see that the ZFS commands are really easy to use but very powerful, because of this I find it easy to write scripts to do the things I need. Here is some code that I use for snapshots, it's written in python but can be ported to anything as it's taking command line output and parsing info for what it needs.

## Making Snapshots:
This code is used to make snapshots of all the file systems on a zpool. Just edit the zpoolName to be the name of the zpool you want to work with. The main command line in code is `zfs list -o name | grep zpoolName` which outputs a list of filesystems onto the zpool which is used in the code to make snapshots with a timestamp in the snapshots name.


```python
#!/usr/local/bin/python
#Used to make snapshot of all the file systems on a zpool.

import commands
import subprocess
import time
import os

timestamp = time.strftime("%Y%m%d-%H%M")

zpoolName = "storage"
zfsList = commands.getoutput("zfs list -o name | grep %s/" % zpoolName)

for zfsFileSystems in zfsList.split("\n"):
        print "Snapshoting-> %s" % (zfsFileSystems)
        commands.getoutput("zfs snapshot %s@%s" % (zfsFileSystems, timestamp))
```

## Removing Snapshots:
This code is paired with the one that takes the snapshots. It will remove old snapshots after a set number of days by reading the timestamp in the snapshots name. The main command here is `zfs list -H -t snapshot | awk '{print $1}' | grep zpoolName` which should output a list of all the snapshots on the zpoolName.

```python
#!/usr/local/bin/python
#Used to remove old snapshots of all the file systems on a zpool.

import commands
import subprocess
import time
import datetime

now = datetime.datetime.now()
zpoolName = "storage"

zfsList = commands.getoutput("zfs list -H -t snapshot | awk '{print $1}' | grep %s/" % zpoolName)

for zfsSnapshot in zfsList.split("\n"):
        dateSnapshot = datetime.datetime.strptime(zfsSnapshot.split("@")[1], "%Y%m%d-%H%M")
        if (now - dateSnapshot) >= datetime.timedelta(days = 30):
                print "Removing-> %s" % (zfsSnapshot)
                commands.getoutput("zfs destroy %s" % (zfsSnapshot))
```

Open to comments or any ideas to make my code better.
