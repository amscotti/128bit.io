---
author: Anthony Scotti
date: 2010-07-30T00:00:00Z
email: anthony.m.scotti@gmail.com
tags:
- Entitize
- Groovy
- Howto
- Strings
title: Entitize Strings with Groovy
url: /2010/07/30/entitize-strings-with-groovy/
---

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
&amp;#8364; 1250
```
I’m stilling trying to learn Groovy so if anyone knows a better way of doing this please share, also feedback and questions are welcome!
