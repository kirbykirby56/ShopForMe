import scrapy
import re

class GoogleSpider(scrapy.Spider):
    name = 'googlespider'
    output = False;
    def __init__(self, searchTerms='', log=False, **kwargs):
        print(searchTerms)
        output = log
        searchTerms.replace(" ", "+");
        re.sub(' ', "+", searchTerms)
        print(searchTerms)
        self.start_urls = [("http://www.google.com/search?q=" + searchTerms + "&tbm=shop")] #Open google.com/search?<SEARCH+TERMS>&tbm=shop, the shopping tab for that search.
        print(self.start_urls)
        print(searchTerms)
        print("Http://www.google.com/search?" + searchTerms + "&tbm=shop")
        print("\n\n\n\n\n")
        
    def parse(self, response):
        print("\n" + response.url + "\n")
        #print(response.body)
        resList = response.css("#ires > ol > div > div > div").extract()#.extract_first())
        if self.output:
            for item in resList:
                print(item)
                print("\n")
        for item in response.css("#ires > ol > div"):
            name = item.css("div > a > img::attr(alt)").extract_first()
            price = item.css("div:nth-child(2) > div > b::text").extract_first()
            link = item.css("div > a::attr(href)").extract_first()
            link = "https://www.google.com" + link
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
        nex = response.css("#foot > table > tr > td:last_child > a > span:last_child::text").extract_first()
        if nex == "Next":
            next_page_url = str("http://www.google.com" + str(response.css("#foot > table > tr > td:last_child > a::attr(href)").extract_first()));
            if self.output:
                print(next_page_url)
        else :
            next_page_url = None
        if next_page_url is not None and next_page_url is not "http://www.google.com":
            yield scrapy.Request(response.urljoin(next_page_url))
