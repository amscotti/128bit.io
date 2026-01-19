Title: Loggly Archives into MongoDB
Date: 2012-02-15 00:00
Slug: 2012/02/15/loggly-archives-into-mongodb
Save_as: 2012/02/15/loggly-archives-into-mongodb/index.html
URL: 2012/02/15/loggly-archives-into-mongodb/
Tags: Heroku, Howto, Loggly, MongoDB, noSQL
Summary: A Ruby script for archiving Loggly logs into MongoDB using Heroku worker. Fetches archived log files from Loggly API using HTTParty, processes and stores them as documents in MongoDB with metadata about source and timestamp, demonstrating NoSQL storage for log data.

![Loggly Logo](/images/logo/loggly_logo.png)

[Loggly](http://loggly.com) is a great cloud service for managing log files from servers or many servers. It's also an add-on for your Heroku hosted app. Loggly comes in different tiers from a free to monthly service based on how much data you store on Loggly servers. Being cheap, I have picked the free tier for [amscotti.com](http://amscotti.com/) as it's not a mission critical app and I don't have tons of logs. One of the coolest things I like about Loggly is they do 'Log Archiving' on Amazon's S3 for you. All you need to do is setup a bucket on S3 and update some settings into the Loggly UI.

The files they push out to S3 are JSON files that have been gzip'ed and are in folders based on year/month/day. There is a easy way to push their files in to MongoDB just using some nice Unix tools and MongoDB's importer.

Download all the files you want to push to MongoDB, you can leave the files in the folder they are in. No need to move them around but there also isn't harm in it. There are many tools you can do this with, myself I use Cyberduck and just drag and drop the folder on my desktop. Keep in mind that the files for the current date and time are still being written out and could give you errors when you try to copy them. Best to not copy them.

Now we need to get the files into a format that MongoDB's importer can read. Lucky the importer can read JSON along with other formats so we don't need to do too much work. I find this can be done with one command. Ensure that you're in the root folder for all the files you want to import into MongoDB and run this,
```
find . -type f -name "*json.gz" | xargs gzcat >> output_file.json
```
You should now have a file of all the logs in JSON format. Depending on your system you may be able to use zcat instead of gzcat.

The next part is the import into MongoDB, again this can be done with one command.
```
mongoimport -d loggly -c amscotti output_file.json --jsonArray
```
The -d is the database you want to use and the -c is the collection you want the data to be imported in to. Due to the format of the file you need the `--jsonArray`. I don't have many logs, I have about 8816 lines in the file and it took less then a second to import into the database.

After that all your data is imported and you are good to go, your now able to run map reduce on your log files to your heart's content!

If you have any questions or comments please post, also any suggestions on improving this are welcome.
