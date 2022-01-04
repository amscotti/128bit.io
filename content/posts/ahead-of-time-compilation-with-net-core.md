---
title: "Ahead-Of-Time Compilation With .Net Core"
date: 2020-10-25T20:56:42-04:00
draft: false
tags:
- FSharp
- CSharp
- Dotnet
- Development
---

I'm still on my journey with exploring F# but I want to look at something with the .Net Core platform itself, so this will apply to both C# and F#. Ahead-Of-Time (AOT) compilation isn't a new concept. Languages like C and C++ need to be compiled before (or ahead of) execution time. The JVM and CLR took a different approach, creating "virtual machines" or runtimes that could run your code, giving us the promise of "[write once, run anywhere](https://en.wikipedia.org/wiki/Write_once,_run_anywhere)" or anywhere that has a virtual machine at least. This idea was good as the runtime could help manage memory and provide optimizations as the code runs. Other languages took this same approach, like JavaScript, Python, Ruby, and Erlang. 

There is nothing wrong with this approach, and in many ways it's a great system. Still, if we look at some "newer" programming languages like Rust and Go, they can compile your code into a single executable that does not require a runtime environment to execute your code. People have found that having just a single executable file was vastly easier to deploy or ship to users. This technique has also become quite popular with Microservices and some successful open-source projects like [Docker](https://www.docker.com), [CockroachDB](https://www.cockroachlabs.com), [Prometheus](https://prometheus.io), and [Consul](https://www.consul.io).

Looking into the Java world, Oracle has developed a new runtime called [GraalVM](https://www.graalvm.org). This runtime has a lot of things it's trying to do. One of the prominent features is "native image" functionality, allowing the creation of an ahead-of-time compilation of Java code into a standalone executable. Testing this on some of my smaller projects seems to be hit or miss at this point, especially for Clojure. 

GraalVM's native image is something people are interested in; you can see this from developers maintaining compatibility with two new frameworks for writing Microservices [Quarkus](https://t.co/8EJ7UFEXK4?amp=1) and [Micronaut](https://micronaut.io/). Using native image will reduce the start-up time and use less memory. Still, there is a trade-off. In some cases, your application will run slower or restrict what libraries you can use. Yet, these may be acceptable trade-offs in the world of Microservices, especially when thinking about lambda type services that benefit significantly from a faster start time.

{{< youtube J9oJTKwASjA >}}
[.NET Conf - Focus on Microservices](https://www.youtube.com/watch?v=J9oJTKwASjA)

Talking about Microservices, I watched the .Net Core Conference on Microservices a while ago and the topic of AOT compilation came [up about 50 mins into the event's video](https://youtu.be/J9oJTKwASjA?t=3012). I never realized that AOT compilation is something that is currently built into .NET Core. The video shows how you can create single executables that are smaller in size. It's quite simple; using the `dotnet publish` command, you can create a single executable for a target platform. Here is the command for creating a Windows 64-bit application, 

`dotnet publish -r win-x64 -c release /p:PublishSingleFile=true /p:PublishTrimmed=true`

For other platforms, you will need to change `win-x64` to something else. For example, if you want to target macOS, `osx-x64` is most likely what you want. I also tested out a cross-platform compilation by creating a Linux executable on my Windows 10 64-bit system. Here is a full list of Runtime Identifier found on [.NET Core Runtime Identifier (RID) catalog | Microsoft Docs](https://docs.microsoft.com/en-us/dotnet/core/rid-catalog)

I have tested this process on some small console applications that use third-party libraries without any issues. Overall, I had a better experience creating executables than I did with GraalVM. I'm sure there are some limitations, but I have not hit them in my testing. In the video of .NET Conf, they use this technique to create a single executable for an ASP.NET Core "Hello World" application.

For myself, I create a lot of command-line tools and being able to create single executable files is very lovely, more so if I can use a functional programming language like F#. It's also great that you already have everything you need to start creating single executable applications if you have already been developing with the .NET Core platform.