---
title: "New Home and a puppy too!"
date: 2023-03-10T13:32:45-05:00
draft: false
tags:
- Home
- Puppy
- IoT
- Home Assistant
- Linux
---
I've never been great at keeping up with blogging, but I believe it's important, especially as a software engineer as it exercises our ability to document and write things down. I typically blog when I have free time and my mind isn't focusing on other things. As I've taken a vacation day today, I figured it would be a good time to dust off my blog and talk about what's been keeping me from posting, but also things that continue to interest me with the hope that it can spark some excitement for new postings.

One big item that has been taking up a lot of my time, but I'm very happy about, is buying a home. Despite the crazy market, my wife and I were able to find a beautiful old home at a price that we were happy with. It has been an adventure updating various areas of the house to make it our own and discovering its secrets. Of course, I've also been modernizing the house with IoT devices, including[ EcoBee thermostats](https://www.ecobee.com/en-us/), [Philips Hue lights](https://www.philips-hue.com/en-us), [Kasa Wifi switches](https://www.kasasmart.com/us/products/smart-switches/kasa-smart-wi-fi-light-switch-hs200) and [smart plugs](https://www.kasasmart.com/us/products/smart-plugs), Google Nest floodlights and doorbells, and devices to monitor our water and electrical usage. I have also worked on improving the connectivity of the house by installing a [Dream Machine SE](https://store.ui.com/collections/unifi-network-unifi-consoles/products/dream-machine-se) from Ubiquiti and Wifi 6 access points while running [Cat 6A cables](https://www.amazon.com/gp/product/B073WMTQ3R/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) throughout the house. For the first time ever, I'm able to achieve the maximum download speed from my internet service provider on my desktop and while I understand that there's no practical use for having extreme download speeds, it's still a fun achievement.

{{< image src="/images/new-home-and-puppy/home_2023.png" alt="Photo of our home" position="center" style="border-radius: 8px;" >}}

Aside from having fun with the house, we recently welcomed a rescue puppy into our home who has been filling our time with lots of fun playing chase and training. She's incredibly adorable and has a wonderful personality.

{{< image src="/images/new-home-and-puppy/eva_2023.png" alt="Photo of Eva looking cute" position="center" style="border-radius: 8px;" >}}

Despite having limited time, I'm constantly looking into new things to learn and explore. Here is a glimpse of some of the things that are currently exciting to me:

At the push of my brother and with the addition of IoT devices to the house, I have been exploring [Home Assistant](https://www.home-assistant.io/) for automation and data gathering. Home Assistant provides platform independence, meaning it doesn't rely on Amazon or Google, and is self-hosted locally. I currently have Home Assistant set up on a small [Proxmox](https://www.proxmox.com/en/) server following these wonderful [instructions](https://community.home-assistant.io/t/installing-home-assistant-os-using-proxmox-7/201835). While many people use Raspberry Pis for their Home Assistant setup, I decided to use Proxmox as I already had it set up and running. I'm still learning about Home Assistant and getting things set up, but I find the data that can be gathered and the flexibility across devices to be very nice.

I'm still heavily focused on learning functional programming, with a particular focus on [Clojure](https://clojure.org/), but I'm also interested in exploring [Haskell](https://www.haskell.org/) or [OCaml](https://ocaml.org/) (or some variant, like [ReScript](https://rescript-lang.org/)) in the future. In addition to functional programming languages, I have been playing around with [Go](https://go.dev/) and [Rust](https://www.rust-lang.org/), both of which are great languages in their own right but Rust provides a lot of features that I enjoy from functional programming languages, along with excellent support for WebAssembly, including for System Interface (WASI). I believe that there are a lot of great things coming out of the WebAssembly space, even outside of browsers.

The last thing I've been looking into is immutable Linux distributions, such as [Fedora Silverblue](https://silverblue.fedoraproject.or), [openSUSE MicroOS](https://microos.opensuse.org/), and [Vanilla OS](https://vanillaos.org/). Immutable distributions are designed to be more secure and easier to manage, by treating the entire operating system as a single, immutable unit. This means that the operating system is read-only and cannot be modified, which helps to prevent accidental changes or malicious attacks. For years, I spent most of my time using Linux with Windows installed for various things, but mostly for gaming. For over a year now, I have fully switched over to Linux, using [Pop! OS](https://pop.system76.com/), and haven't had any need to switch back to Windows. The applications I use and games I play have been running excellent on Linux. While I'm not one for distro hopping, I think there are enough advantages to start taking a look at immutable Linux distributions. After testing using [Flatpaks](https://www.flatpak.org/) and [Distrobox](https://github.com/89luca89/distrobox) on Pop! OS, I feel like I wouldn't hit too many roadblocks switching to one of the immutable Linux distributions. If you're also interested in this, [Jorge Castro](https://www.youtube.com/@JorgeCastro) has some great videos on YouTube about this idea, mostly around using Fedora Silverblue. When I have some downtime, I definitely want to explore using immutable Linux distributions, with MicroOS being my first choice.

{{< youtube PM5exNztbXE >}}

I think this is a good start of trying to blog again, with some great jumping off points for some small more focused postings in the future. Until next time!