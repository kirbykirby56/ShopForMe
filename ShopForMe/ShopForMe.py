import scrapy
import re

class GoogleSpider(scrapy.Spider):
    name = 'googlespider'
    output = True;
    def __init__(self, searchTerms='', log=True, **kwargs):
        output = log
        re.sub(' ', "+", searchTerms)
        self.start_urls = [("http://www.google.com/search?q=" + searchTerms + "&tbm=shop")] #Open google.com/search?<SEARCH+TERMS>&tbm=shop, the shopping tab for that search.
        print("Start Urls: " + self.start_urls[0]) if self.output else None
            
    def parse(self, response):
        print(response.url) if self.output else None
        for item in response.css("#ires > ol > div"):
            name = item.css("div > a > img::attr(alt)").extract_first()
            price = item.css("div:nth-child(2) > div > b::text").extract_first()
            link = "https://www.google.com" + item.css("div > a::attr(href)").extract_first()
            re.sub("&amp", "&", link)
            print("    NAME: " + name + "\n    LINK: " + link + "    PRICE: " + price + "\n" if self.output else "")
            yield {
                'Name': name,
                'Price': price,
                'Link': link
            }
            next_page_url = str("http://www.google.com" + str(response.css("#foot > table > tr > td:last_child > a::attr(href)").extract_first())) if response.css("#foot > table > tr > td:last_child > a > span:last_child::text").extract_first() == "Next" else None #If there's a "Next" button, it's the link it points to, else nothing.
            yield scrapy.Request(response.urljoin(next_page_url)) if next_page_url is not None else None
