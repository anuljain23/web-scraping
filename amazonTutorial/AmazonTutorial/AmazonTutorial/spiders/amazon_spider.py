import scrapy
from ..items import AmazontutorialItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1594763717&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0'
    ]
    def parse(self,response):
        items = AmazontutorialItem()
        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base.a-link-normal::text, .a-size-base+ .a-size-base:nth-child(6)::text, .sg-col-12-of-28 span:nth-child(2)::text').extract()
        product_price = response.css('.a-spacing-top-small .a-price-whole::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items
