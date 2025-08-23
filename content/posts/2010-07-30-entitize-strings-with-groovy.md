Title: Entitize Strings with Groovy
Date: 2010-07-30 00:00
Slug: 2010/07/30/entitize-strings-with-groovy
Save_as: 2010/07/30/entitize-strings-with-groovy/index.html
URL: 2010/07/30/entitize-strings-with-groovy/
Tags: Entitize, Groovy, Howto, Strings
Summary: A Groovy function demonstrating how to replace high-level Unicode characters with their HTML entity equivalents. The entitize function iterates through a string, converting characters with code points above 127 to numeric character references like &#8364; for the Euro symbol, useful for HTML/XML output.

Not sure if 'entitize' is the right term but it's what people at my old job would call the process of taking high level characters and replacing them with the unicode. For example, € would be replaced with &amp;#8364;. This was needed with some inhouse applications or dealing with output to HTML/XML to ensure it would show the right character to the users. Well, I needed to do this awhile ago and I looked up some old Python code that I had done before and re-wrote it in Groovy. So here is the code snippet.

```
def entitize(dirty_string) {
	def clean_string = ""
	dirty_string.each { it ->
		def ordcode = it.codePointAt(0)
		if (ordcode > 127){ clean_string += "&#${ordcode};" } else { clean_string += it }
	}
	return clean_string
}
```

So, this
```
println entitize("Test Test")
println entitize("€ 1250")
```
Should output this,
```
Test Test
&#8364; 1250
```
I’m stilling trying to learn Groovy so if anyone knows a better way of doing this please share, also feedback and questions are welcome!
