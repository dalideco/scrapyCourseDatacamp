from scrapy import Selector
import requests

html =requests.get("http://my-portfolio-dalideco.herokuapp.com/").content

sel = Selector(text = html)
text = sel.xpath('/html').extract()
print(text)

#can't extract from my portfolio cuz it's react compiled to javascript code and not html