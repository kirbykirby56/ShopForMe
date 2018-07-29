import scrapy
import re

class GoogleSpider(scrapy.Spider):
    name = 'googlespider'
    output = False;


    def __init__(self, searchTerms='', log=False, **kwargs):
        output = log
        searchTerms.replace(" ", "+")#It's probably true that one of these does all of the work, but I have both so that it's guaranteed to work anyway.
        re.sub(' ', "+", searchTerms)
        self.start_urls = [("http://www.google.com/search?q=" + searchTerms + "&tbm=shop")] #Open google.com/search?<SEARCH+TERMS>&tbm=shop, the shopping tab for that search.
        if self.output:
            print("Start Urls: ")
            print(self.start_urls)
            print("\n")


    def parse(self, response):
        if self.output:
            print(response.url + "\n")
        for item in response.css("#ires > ol > div"):
            name = item.css("div > a > img::attr(alt)").extract_first()
            price = item.css("div:nth-child(2) > div > b::text").extract_first()
            link = "https://www.google.com" + item.css("div > a::attr(href)").extract_first()
            re.sub("&amp", "&", link)
            if self.output:
                print("NAME: " + name)
                print("LINK: " + link)
                print("PRICE: " + price),
            yield {
                'Name': name,
                'Price': price,
                'Link': link
            }
        if response.css("#foot > table > tr > td:last_child > a > span:last_child::text").extract_first() == "Next": #This will run until there's no "next" button.
            next_page_url = str("http://www.google.com" + str(response.css("#foot > table > tr > td:last_child > a::attr(href)").extract_first()));
        else :
            next_page_url = None
        if next_page_url is not None and next_page_url is not "http://www.google.com":
            yield scrapy.Request(response.urljoin(next_page_url))
