---
author: Anthony Scotti
date: 2010-05-31T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Encryption
- Howto
- Linux
- OpenSSL
- UNIX
title: File Encryption with OpenSSL
url: /2010/05/31/file-encryption-with-openssl/
---

Time to time you may find the need to encrypt a file before sending it to someone or store it where other people may have access to it. OpenSSL is a great tool for this and it is installed on most Linux/Unix and OS X (also, I believe there is an install for OpenSSL for Windows too).

Here's the command to encrypt a file,

```
$ openssl enc -aes-256-cbc -a -salt -in mytestfile.txt -out myencryptedtestfile.txt
```

It will ask you for a password and then encrypt the file.

To decrypt,

```
$ openssl enc -d -aes-256-cbc -a -in myencryptedtestfile.txt -out unencryptedmytestfile.txt
```

You can also pipe in data in and out of OpenSSL by removing the -in or -out (or both) like so,

```
$ cat mytestfile.txt | openssl enc -aes-256-cbc -a -salt -out myencryptedtestfile.txt
```

```
$ cat myencryptedtestfile.txt | openssl enc -d -aes-256-cbc -a -out unencryptedmytestfile.txt
```
You are also able to use different encryption algorithms with OpenSSL as long as you encrypt and decrypt using the same algorithms.

Open for questions, comments, or any way to improve this!
