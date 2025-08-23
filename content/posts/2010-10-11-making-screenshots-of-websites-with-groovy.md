Title: Making screenshots of websites with Groovy
Date: 2010-10-11 00:00
Slug: 2010/10/11/making-screenshots-of-websites-with-groovy
Save_as: 2010/10/11/making-screenshots-of-websites-with-groovy/index.html
URL: 2010/10/11/making-screenshots-of-websites-with-groovy/
Tags: Groovy, Howto, Java, JTidy, Renderer, XHTML, XML
Summary: A Groovy port of Java code for generating website screenshots. Uses JTidy to convert HTML to XHTML and the Flying Saucer renderer to output PNG images, demonstrating how to programmatically capture thumbnails of websites for archiving or preview purposes.

For a project I needed to work out a way to make thumbnails/screenshots of HTML files for some Java code I was working on. From my research, I found a nice project called the [The Flying Saucer Project](https://xhtmlrenderer.dev.java.net/) which has an XML/XHTML/CSS 2.1 renderer which works for what I needed for my project. Taking the HTML files and using [JTidy](http://jtidy.sourceforge.net/) to make them in to XHTML the renderer could output an image file for me. You are also able to use the renderer to make PDFs and SVG files. I wanted to take the small part of my code that was written in Java and port it over to Groovy. As I'm still learning Groovy I'm sure there is way to make this code better and I would love some feedback!

Here is the code,

```groovy
import java.awt.Dimension
import java.awt.Graphics2D
import java.awt.RenderingHints
import java.awt.image.BufferedImage
import javax.imageio.ImageIO
import org.w3c.dom.Document
import org.w3c.tidy.Tidy
import org.xhtmlrenderer.simple.Graphics2DRenderer

def makeThumbnail(address) {
  // Size for the renderer
	def WIDTH = 1280
	def HEIGHT = 800

	// Setup Tidy
	def tidy = new Tidy()
	tidy.with {
		setQuiet(true)
		setXHTML(true)
		setHideComments(true)
		setInputEncoding("UTF-8")
		setOutputEncoding("UTF-8")
		setShowErrors(0)
		setShowWarnings(false)
	}

	def url = new URL(address)
	def doc = tidy.parseDOM(new ByteArrayInputStream(url.text.getBytes("UTF-8")), null)
	def os = new FileOutputStream("/Users/ascotti/${url.getHost()}.png")

	def buf = new BufferedImage(WIDTH, HEIGHT, BufferedImage.TYPE_INT_RGB)

	def graphics = buf.createGraphics()
	def renderer = new Graphics2DRenderer()

	renderer.with {
		setDocument(doc, address)
		layout(graphics, new Dimension(WIDTH, HEIGHT))
		render(graphics)
		graphics.dispose()
		ImageIO.write(buf, "png", os)
	}
}

makeThumbnail("http://www.128bitstudios.com/")
makeThumbnail("http://en.wikipedia.org/")
makeThumbnail("http://misplaced-packets.net/")
makeThumbnail("http://stackoverflow.com/")
```

Here is the output from the code,

**www.128bitstudios.com**

![www.128bitstudios.com](/images/making-screenshots-of-websites-with-groovy/www.128bitstudios.com_-300x187.png)

**en.wikipedia.org**

![en.wikipedia.org](/images/making-screenshots-of-websites-with-groovy/en.wikipedia.org_-300x187.png)

**misplaced-packets.net**

![misplaced-packets.net](/images/making-screenshots-of-websites-with-groovy/misplaced-packets.net_-300x187.png)

**stackoverflow.com**

![stackoverflow.com](/images/making-screenshots-of-websites-with-groovy/stackoverflow.com_-300x187.png)

As you can see the output isn't perfect but if you are just making thumbnails it should be ok. It has issues when it comes to java script which on some sites are used for layout. If you have a site/HTML file that just uses HTML and CSS the output should be good. I would love someone that is better acquainted with Groovy to over look this for way to make the code more 'groovify'.

Open for questions, comments, or any way to improve this!
