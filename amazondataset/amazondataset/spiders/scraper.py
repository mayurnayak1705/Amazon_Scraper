import random
import scrapy
from gc import callbacks
from amazondataset.items import ProductItems

class ScraperSpider(scrapy.Spider):
    name = "scraper"
    allowed_domains = ["amazon.in"]

    base_url="https://www.amazon.in/s?k="
    search_query=input("Enter the search keyword/string for the dataset you want to obtain===>")
    formatted_query = '+'.join(search_query.split())

    start_urls = ["https://www.amazon.in/s?k="+formatted_query]

    user_agent_list=[
        'Mozilla/5.0 (Linux; Android 13; SM-A536U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 13; SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 12; moto g pure) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 12; moto g 5G (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
    ]
   
    
    def parse(self, response):
        all_products=response.css("div.sg-col-4-of-24.sg-col-4-of-12.s-result-item.s-asin.sg-col-4-of-16.sg-col.s-widget-spacing-small.sg-col-4-of-20") 
        for product in all_products:
            href_url=product.css("h2 a ::attr(href)").get()
            product_url="https://www.amazon.in"+href_url
            # yield response.follow(product_url, callback=self.parse_product, headers={"User-Agent": self.user_agent_list[random.randint(0,len(self.user_agent_list)-1)]})
            yield response.follow(product_url, callback=self.parse_product)

        print(response.url)
        relative_url=response.css("a.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator::attr(href)").get()
        if relative_url is not None:
            next_page_url="https://www.amazon.in"+relative_url
            # yield response.follow(next_page_url, callback=self.parse,ssheaders={"User-Agent": self.user_agent_list[random.randint(0,len(self.user_agent_list)-1)]})
            yield response.follow(next_page_url, callback=self.parse)


    def parse_product(self, response):

        product_item=ProductItems()

        product_item['url'] = response.url,
        product_item['product_name'] = response.css("h1 span::text").get(),
        product_item['product_price'] = response.css("span.a-price-whole::text").get(),
        product_item['percentage_off'] = response.css("span.a-size-large.a-color-price.savingPriceOverride.aok-align-center.reinventPriceSavingsPercentageMargin.savingsPercentage::text").get(),
        product_item['orignal_price'] = response.css("span.a-price.a-text-price span::text").get(),
        product_item['ratings'] = response.css("span.a-icon-alt::text").get(),
        product_item['image_url'] = response.css("div.imgTagWrapper img::attr(src)").get(),
        product_item['product_description'] = response.css("div.a-section.a-spacing-small p span::text").get(),
                
        yield product_item

        # yield {
        #     'url' : response.url,
        #     'title' : response.css('.product_main h1::text').get(),
        #     'product_type': response.css("h1 span::text").get(),
        #     'num_reviews': response.css("span.a-icon-alt::text").get(),
        #     'description' : response.css("div.a-section.a-spacing-small p span::text").get(),
        #     'price':response.css("span.a-price-whole::text").get(),
        # }

        
        
            






