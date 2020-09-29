# -*- coding: utf-8 -*-
import scrapy


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
    'https://www.simplyhired.com/search?q=&l=Austin%2C+TX&job=rL-FPHmOlO8S0LDRzJZQ1C1-GcuCOZ1Z6Au5yRSFG3M7X_c1ZcOmGA'
    ]

    BASE_URL = 'https://www.simplyhired.com'

    def parse(self, response):
         links = response.css('a.card-link').xpath("@href").extract()
         for link in links:
            absolute_url = self.BASE_URL + link
            yield scrapy.Request(absolute_url, callback=self.parse_attr)
         next_page = "https://www.simplyhired.com/search?l=Austin%2C+TX&pn="+str(DmozSpider.page_number)+"&job=380F5vdkwZikDiGf3s4a_3eH3-C2X4PGkJbB_JUmDwV0XnuKtWRJjw"

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
        item["Title"] = response.css("h2.viewjob-jobTitle::text").extract() 
        item["Location"] = response.css("div.viewjob-labelWithIcon::text")[1].extract()
        item["Company"] = response.css("div.viewjob-labelWithIcon::text")[0].extract()
        aa=response.css("div.p::text").extract()
        text_list=""
        for text in aa:
            text = text.rstrip("\n")
            text_list=text_list+text
        item["Description"] = text_list
        item["ApplyLink"] = response.url
        item["salary"]=response.css("span.viewjob-labelWithIcon::text").extract()
        
        return item