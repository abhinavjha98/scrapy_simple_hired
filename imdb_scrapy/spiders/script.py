# -*- coding: utf-8 -*-
import scrapy
import urllib
import requests

# item class included here 
class DmozItem(scrapy.Item):

    # define the fields for your item here like:
    ApplyLink = scrapy.Field()
    Title = scrapy.Field()
    Company = scrapy.Field()
    Location = scrapy.Field()
    salary = scrapy.Field()
    Logo = scrapy.Field()
    Description = scrapy.Field()



class DmozSpider(scrapy.Spider):
    name = "dmoz"
    page_number = 2
    start_urls = [
    'https://www.simplyhired.com/search?q=java&l=Philadelphia%2C+PA&job=fYxbZPaOvxUi_StIPQGdAhmm__9ReBI5jbVy7amchpkhgoG5xdkwUA'
    ]

    BASE_URL = 'https://www.simplyhired.com'

    def parse(self, response):
         links = response.css('a.card-link').xpath("@href").extract()
         for link in links:
            absolute_url = self.BASE_URL + link
            yield scrapy.Request(absolute_url, callback=self.parse_attr)
         next_page = "https://www.simplyhired.com/search?q=java&l=Philadelphia%2C+PA&pn="+str(DmozSpider.page_number)+"&job=fYxbZPaOvxUi_StIPQGdAhmm__9ReBI5jbVy7amchpkhgoG5xdkwUA"

         if DmozSpider.page_number<=91:
            DmozSpider.page_number +=1
            yield response.follow(next_page,callback=self.parse)

    def parse_attr(self, response):
        item = DmozItem()
        logo = response.css('img.viewjob-company-logoImg').xpath("@src").extract()
        try:
            item["Logo"] = DmozSpider.BASE_URL+""+logo[0]
        except:
            item["Logo"] = 'none'
        item["Title"] = response.css("div.viewjob-jobTitle::text").extract() 
        item["Location"] = response.css("div.viewjob-labelWithIcon::text")[1].extract()
        item["Company"] = response.css("div.viewjob-labelWithIcon::text")[0].extract()
        aa=response.css("div.p::text").extract()
        text_list=""
        for text in aa:
            text = text.rstrip("\n")
            text_list=text_list+text
        item["Description"] = text_list
        links = response.css('a.btn-apply').xpath("@href").extract()
        # final_url = urllib.request.urlopen("https://www.simplyhired.com"+links[0],None,1).geturl()
        final_url = requests.get("https://www.simplyhired.com"+links[0])
        item["ApplyLink"] = final_url.url
        item["salary"]=response.css("span.viewjob-labelWithIcon::text").extract()
        
        return item