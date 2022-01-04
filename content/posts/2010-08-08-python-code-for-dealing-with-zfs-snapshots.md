---
author: Anthony Scotti
date: 2010-08-08T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- FreeBSD
- Howto
- Opensolaris
- Python
- Solaris
- ZFS
title: Python code for dealing with ZFS snapshots
url: /2010/08/08/python-code-for-dealing-with-zfs-snapshots/
---

From my last posting about ZFS "[Fun with ZFS send and receive]({{< relref "2010-07-23-fun-with-zfs-send-and-receive.md" >}})" we see that the ZFS commands are really easy to use but very powerful, because of this I find it easy to write scripts to do the things I need. Here is some code that I use for snapshots, it's written in python but can be ported to anything as it's taking command line output and parsing info for what it needs.

## Making Snapshots:
This code is used to make snapshots of all the file systems on a zpool. Just edit the zpoolName to be the name of the zpool you want to work with. The main command line in code is `zfs list -o name | grep zpoolName` which outputs a list of filesystems onto the zpool which is used in the code to make snapshots with a timestamp in the snapshots name.


{{< gist amscotti 5473914 "zfs_make_snapshots.py" >}}

## Removing Snapshots:
This code is paired with the one that takes the snapshots. It will remove old snapshots after a set number of days by reading the timestamp in the snapshots name. The main command here is `zfs list -H -t snapshot | awk '{print $1}' | grep zpoolName` which should output a list of all the snapshots on the zpoolName.

{{< gist amscotti 5473914 "zfs_remove_snapshots.py" >}}

Open to comments or any ideas to make my code better.
