Title: Hugo and Netlify
Date: 2017-08-20 20:22
Slug: hugo-and-netlify
Tags: Hugo, Netlify, Blog
Summary: Migration from Jekyll on S3 to Hugo static site generator with Netlify CDN hosting. Discusses Hugo's easy Jekyll import, Go language benefits, theme customization, fast setup. Praises Netlify's simple GitHub integration, free SSL certificates, custom domain support, and web UI configuration for HTTPS redirects, calling setup smoother than previous S3/CloudFront.

So, it was time for a bit of change for the blog. I have been using an older version of Jekyll for some time and upgrading for me has always been a pain. I picked to move away from Jekyll to something new, this is where Hugo comes into play.

![Netlify+Hugo=<3](/images/hugo-and-netlify/hugonetlifylove.png)

## Hugo

[Hugo](https://gohugo.io/) is another static site generator like Jekyll but written in Go, it boasts itself as the fastest tool of its kind but it wasn't the speed that drew me to it. The thing that drew me to Hugo was the ease of importing my pre-existing Jekyll blog with one command. After the import, I had a 90% ready to use Hugo blog.

Hugo being written in Go does give it more than just the speed advantage over Jekyll, Go compiles down to a single binary that makes it extremely easy to install and run. This was another win over Jekyll for me when it comes to setting up a system.

After getting a nice looking theme, [some regex magic](https://xkcd.com/208/), along with small edits to some postings, I was all set. Now it's time to think about hosting.

## Netlify

The old blog was hosted on S3 with CloudFront, this is a great setup and I have used it many times before from other blogs to company websites. You generally have a nice speedy page that you can point a domain at and even get a free SSL certificate for. It works, and it's not bad but it never felt right to me.

One of the things that bugged me about this setup was needing to use the [s3_website](https://github.com/laurilehmijoki/s3_website) gem. It's great software, but you need to have Java installed on the system to make use of it. So, your install base needs both Ruby and Java, which isn't bad for a developer's machine but is painful for a [Docker Image](/2017/01/10/Building-a-Docker-Image-for-BitBucket-Pipelines/). Besides that, I had SSL setup but CloudFront will not enforce it. You need to add some Javascript to redirect people to HTTPS. Overall S3 and CloudFront can be kind of convoluted and not straightforward for something as simple as a blog.

This is where [Netlify](https://www.netlify.com/) helps out, Netlify is a CDN for static websites. They make it easy for people to deploy their projects, overall it took me maybe 5 minutes to get everything all set. I never used Netlify before, I found out about them from other people talking about using them for hosting Hugo blogs. For everything I need, like custom domains, and SSL, I get that for free along with TLS enforcement.

Setup was easy as pointing Netlify to my GitHub repository and telling them how to build the project. Because they are the CDN and the ones building the project, there isn't any need to setup AWS keys or anything type of authorization like that. You can even add a `netlify.toml` and have less configuration through the web UI.

Both Hugo and Netlify are very new to me, so far I have had a great experience with them. We'll see as time goes on, but so far I'm quite happy with these two technologies.

## Resources

* [Host on Netlify](https://gohugo.io/hosting-and-deployment/hosting-on-netlify/)
* [Goodbye WordPress! Hello Static (Hugo) and Netlify (static hosting and more)](https://eran.sandler.co.il/2017/06/04/goodbye-wordpress-hello-static-netlify/)
* [Migrating from Jekyll+Github Pages to Hugo+Netlify](https://www.sarasoueidan.com/blog/jekyll-ghpages-to-hugo-netlify/)
