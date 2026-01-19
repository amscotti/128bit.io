Title: Respect for PHP 🐘
Date: 2023-05-27 17:32
Slug: respect-for-php
Tags: PHP, Development
Summary: Reflection on PHP's historical and ongoing relevance. Discusses LAMP stack era, PHP's simplicity for web development, Apache HTTP Server contributions to the web, Wikipedia/Facebook/Etsy origins, modern ecosystem with Composer/Laravel, and diverse applications like cPanel, WordPress, Drupal, and ad-blocking Pi-hole.

While [PHP](https://www.php.net/) isn't my favorite language by any means, it's one that I've used throughout my career at various points. This fact was recently brought to my attention during a conversation with a colleague about my past experiences. I wouldn't label myself a dedicated PHP developer, but my history with the language stretches back to my college days, when I even completed my senior project using PHP.

After college, PHP continued to play a part in my professional life. I utilized it in various capacities, from building mobile-optimized sites and web services, to my present role where we employ Laravel to create REST APIs that deliver JSON data to our frontend. We also develop event-based systems that leverage the power of Amazon Web Services. As a result, I've had the opportunity to witness PHP's evolution over time, and I believe it's a language that deserves respect.

If you want a quick overview of some of the history of PHP, there is an excellent [video](https://www.youtube.com/watch?v=wCZ5TJCBWMg) from the creator of PHP, [Rasmus Lerdorf](https://en.wikipedia.org/wiki/Rasmus_Lerdorf), from 2019 at [phpday](https://phpday.it/).

## The LAMP Era

There was a time when the acronym "LAMP" was ubiquitous in job postings, as companies sought developers familiar with this popular web development stack. Though the "web" was still in its infancy, PHP provided an accessible way to build websites, which remains hard to compete with even today. As long as you have a web server set up with PHP, all it takes is copying your PHP files to the appropriate folder on the server. This simple, yet elegant, concept made it easy for companies to offer LAMP stack hosting.

The "A" in the [LAMP stack](https://en.wikipedia.org/wiki/LAMP_%28software_bundle%29) stands for Apache HTTP, which featured built-in support for virtual hosts, allowing a single server to support multiple websites. This functionality eventually led to the rise of software like [cPanel](https://www.cpanel.net/), which further simplified the process for both hosting providers and users alike.

## PHP's Ongoing Relevance

Thanks to its ease of use, PHP's popularity soared, leading to the development of countless websites and software projects. When discussing PHP, a few well-known sites and projects often come to mind, such as [Wikipedia](https://www.wikipedia.org/) which uses [MediaWiki](https://github.com/wikimedia/mediawiki) and Facebook, which was originally created in PHP. There a lot of other sites that started with, or still are using PHP like [Flickr](https://www.flickr.com/), [Etsy](https://www.etsy.com/), [Yahoo](https://www.yahoo.com/), [Slack](https://slack.com/), [Tumblr](https://tumblr.com/), [MailChimp](https://mailchimp.com/), and [Wayfair](https://www.wayfair.com/).

When it comes to projects using PHP, two of the most frequently mentioned projects in the context of PHP are [WordPress](https://wordpress.com/) and [Drupal](https://www.drupal.org/), both of which continue to be widely used today but there are many others, and to name a few,

-   [Nextcloud](https://nextcloud.com/) is a popular self-hosted alternative to Google Workspace, offering much of the same functionality.
-   [Wallabag](https://wallabag.org) is a self-hostable application for saving web pages, written in PHP. It also offers a hosted service called [wallabag.it](https://www.wallabag.it/en).
-   [OpenMediaVault](https://www.openmediavault.org/) is a PHP-based software that enables users to create their own NAS (Network Attached Storage) systems.
-   [Pi-hole](https://pi-hole.net/) is an ad-blocking software whose dashboard is written in PHP. It can easily be run on a Raspberry Pi, as the name suggests.

These projects may not be as renowned as WordPress, but they are actively developed and maintained, with a dedicated user base, including myself. The diverse applications of PHP across these projects demonstrate the language's ongoing relevance in today's web development landscape.

## Evolution and Advancements

{% youtube x9bSUo6TGgY %}
[The evolution of PHP](https://www.youtube.com/watch?v=x9bSUo6TGgY)

When I first started using PHP, many applications were unstructured, often consisting of PHP pages for views that would process data, call the database, and display the results in a table. Today, PHP offers comprehensive support for Object-Oriented Programming, type hinting, testing frameworks, linters, and static analysis tools to ensure high-quality code. The ecosystem has matured significantly, with PHP now boasting a robust package management system called [Composer](https://getcomposer.org/) that simplifies the integration of libraries. Additionally, the language now features powerful frameworks like [Laravel](https://laravel.com/) that offer functionality similar to Ruby on Rails in terms of ease of use and developer experience. Looking at the Laravel home page, you can see that it's used by a good number of companies from Twitch to Disney.

{% youtube Spwv0RbITmE %}
[Laravel First Impressions From A JavaScript Dev](https://www.youtube.com/watch?v=Spwv0RbITmE)

Besides these improvements to language features and tooling, PHP's performance has also seen continuous enhancements. PHP had a reputation for being less organized and less performant compared to other languages like Python, JavaScript, and Ruby. However, with the introduction of modern frameworks, PHP has closed this gap and even surpassed some of these languages in certain areas. For instance, [PHP now outperforms Ruby in terms of speed](https://www.techempower.com/benchmarks/#section=data-r21&l=zijx1b-6bj&test=query).

The community has also adapted PHP to be able to use it where they need it, one of these examples which excites me is serverless. Using [Bref](https://bref.sh), you can now use PHP to create serverless applications on [AWS Lambda](https://aws.amazon.com/lambda/) and Bref even lets you leverage existing applications, written in [Laravel](https://laravel.com/) or [Slim](https://www.slimframework.com/).

In many ways, I believe that PHP's evolution mirrors that of JavaScript, albeit several steps behind. The language, tooling, and frameworks have all seen substantial advancements, ultimately providing a developer experience comparable to what one would find working with another language like JavaScript, just within the PHP realm.

## Conclusion

I wrote this article to express my respect for a language that has significantly shaped the web as we know it today, one that is still widely used and has an active community. I've had the opportunity to observe PHP's progress over time and can attest that, with modern PHP, the developer experience is on par with other languages. Though we may not witness a resurgence of PHP's popularity, it remains fascinating to observe its ongoing evolution and advancements, as well as the sharing of ideas among different programming communities to improve their respective languages. This can be seen in other older languages like Java, Python, and Ruby which adopt successful ideas to enhance their capabilities and provide developers with a better experience.

As I mentioned at the start, I wouldn't call myself a PHP developer, nor would I actively seek a role focused on PHP full-time. However, I wouldn't hesitate to work on a project using modern PHP. PHP will always have my respect for the influential role it has played in shaping the digital world.

I do think it's safe for me to say that this will be my last posting on PHP as there many other fun languages that I would like to write about. 😄
