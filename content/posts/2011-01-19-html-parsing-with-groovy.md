Title: HTML Parsing with Groovy
Date: 2011-01-19 00:00
Slug: 2011/01/19/html-parsing-with-groovy
Save_as: 2011/01/19/html-parsing-with-groovy/index.html
URL: 2011/01/19/html-parsing-with-groovy/
Tags: Groovy, Howto, HTML, NFL, Parsing
Summary: Demonstrates how to parse poorly formatted HTML using Groovy with TagSoup library to handle errors. Example code pulls NFL passing statistics from nfl.com by parsing HTML tables and converting them to structured data, with plans to push to a NoSQL database.

In a perfect world all the websites we would go to would be well formatted to the point that we could call them XHML so we could parse the data just like any other XML file but sadly this is not true. There is a lot of errors on pages that your browser fixes in the background or just simply overlooks due to HTML being so lose in its formatting structure. Due to this, the approach of parsing HTML could be a tedious one, but Groovy helps you by letting you call in [TagSoup](http://home.ccil.org/~cowan/XML/tagsoup/) which helps deal with poorly formatted HTML and gives SAX interface that can be used with standard XML tools.

I found myself using this last night trying to parse data from nfl.com for a friend, needing to look at the info in a table and make some kind of usable data structure from it. It turns out to be as easy as parsing a XML file with using TagSoup. Here is a part of the code I used to pull the data and should get you started if you ever find the need to parse some HTML.

```groovy
@Grab(group='org.ccil.cowan.tagsoup', module='tagsoup', version='1.2' )
def tagsoupParser = new org.ccil.cowan.tagsoup.Parser()
def slurper = new XmlSlurper(tagsoupParser)
def url = "http://www.nfl.com/stats/categorystats?archive=false&conference=null&statisticCategory=PASSING&season=2010&seasonType=REG&experience=null&tabSeq=0&qualified=true&Submit=Go"
def htmlParser = slurper.parse(url)

tabledata = htmlParser.'**'.find { it.@class == 'data-table1' }.tbody.tr.collect {
 [
 Rk: it.td[0].text().trim(),
 Player: it.td[1].text().trim(),
 Team: it.td[2].text().trim(),
 Pos: it.td[3].text().trim(),
 Comp: it.td[4].text().trim(),
 Att: it.td[5].text().trim(),
 Pct: it.td[6].text().trim(),
 AttG: it.td[7].text().trim(),
 Yds: it.td[8].text().trim(),
 Avg: it.td[9].text().trim(),
 YdsG: it.td[10].text().trim(),
 TD: it.td[11].text().trim(),
 Int: it.td[12].text().trim(),
 First: it.td[13].text().trim(),
 FirstPercent: it.td[14].text().trim(),
 Lng: it.td[15].text().trim(),
 TwentyPlus: it.td[16].text().trim(),
 FortyPlus: it.td[17].text().trim(),
 Sck: it.td[18].text().trim(),
 Rate: it.td[19].text().trim()
 ]
}

tabledata.each { it ->
 println it
}
```

The output of this isn't that great, this is just to show how you would grab some data from the HTML page using TagSoup along with the @Grab in Groovy. Later I will most likely be pushing this data into a database.... maybe a noSQL database! :)

If you have any questions or comments please post, also any suggestions on improving this are welcome.
