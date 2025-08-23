Title: Making and using SSH Keys
Date: 2010-04-10 00:00
Slug: 2010/04/10/making-and-using-ssh-keys
Save_as: 2010/04/10/making-and-using-ssh-keys/index.html
URL: 2010/04/10/making-and-using-ssh-keys/
Tags: Howto, Linux, SSH, UNIX
Summary: A comprehensive guide to creating and using SSH keys for secure passwordless authentication. Covers key generation, understanding public-key cryptography, key distribution using authorized_keys, and using PuTTY on Windows to enable secure login and automate file transfers without passwords.

Ok, lets start with something easy! :)

## What are SSH keys:

SSH keys are a way to allow someone access to a user on another system without the need for a password. This is done with 2 key files one that is public and the other private. This is called "[Public-key cryptography](http://en.wikipedia.org/wiki/Public-key_cryptography)". The public key will be sent to the server that you want to connect to and the private will stay on your local (or client) system.

## Why use keys:

Using keys add a other layer of security to SSH. You able to have keys needed to log in to your server thus stopping any [brute force attacks](http://en.wikipedia.org/wiki/Brute_force_attack) or you can easily setup a script to copy files over SSH securely without the need for passwords. SSH keys will also help prevent key loggers from reading your login criteria since you don't need a password and you also need the key file to login. Overall, keys are nice way to add security or just make logging in easier and faster!

## Lets start:

Open up the command line and make sure you are in your home folder,

```
$ cd ~
$ pwd
/home/ascotti
```

Now that we are in our home folder we will make sure we have a `.ssh` folder and then generate the keys. On some systems this folder may already be made for you,

```
$ mkdir ~/.ssh
$ chmod 700 ~/.ssh
$ ssh-keygen
```

Now comes the point if you want a passphrase or not. Passphrase acts as a password every time you log into the server. It adds a nice layer of security but is not needed. If you plan on keeping your private key on a USB drive for mobility I would recommend using a passphrase in case you ever lost the USB drive. On the other hand, if you are planning to have this on your local system and have scripts SSH into the server, you most likely don't want a passphrase. Its up to you, just don't forget the passphrase if you enter one.

You know should have 2 files within `~/.ssh`, `id_rsa` and `id_rsa.pub`. The `id_rsa` is your private key and `id_rsa.pub` is the public. The next steps are to sent the public key to the server you wish to connect to.

## Key Distribution:

Now we need to get the public key into the `authorized_keys` on the server we wish to connect to. We want to append to the file as to not overwrite any other keys that may be already set up. This can be done with a nice one line command!

```
$ cat ~/.ssh/id_rsa.pub | ssh username@server "cat >> ~/.ssh/authorized_keys"
```
What is happening here is you are printing out the file with cat having the output go over SSH to the server which will run cat itself and append to the authorized_keys2 file. You will need to enter your password and after you will be disconnected from the server. Give it a quick test by trying to SSH into the server and see if it all works. If you have a passphrase it will ask you for one each time you login.

## PuTTY:

[PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/) is a nice Windows application that lets you SSH into Unix/Linux servers. You are able to use your keys that you made, with the steps above by, using an application that comes with Putty called PuTTYgen. You need to have a copy of your private key `id_rsa` and load the file into PuTTYgen. You made need to change the file type in the file browser to be able to the select the key but it will load it just fine. After loading it, enter your passphrase if you have one and then click 'Save private key' and save the file somewhere safe. You should now be able to use the new file when setting up your connections in PuTTY. On a side note you can also make both private and public if you don't have a Linux system. (But really, who doesn't have a Linux system though!) :P

Open for questions, comments, or any way to improve this!
