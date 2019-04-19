# -*- coding: utf-8 -*-
import scrapy
import re




class TmmSpider(scrapy.Spider):
    name = 'tmm'
    allowed_domains = ['tmall.com']
    start_urls = ['https://list.tmall.com/search_product.htm?q=%D4%CB%B6%AF%D0%AC&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&xl=yundongxi_2&from=mallfp..pc_1_suggest']






    def parse(self, response):
        f = open('123.txt', 'w')
        i=response.xpath('//*[@id="J_ItemList"]/div/div')
        for m  in i:

            temp={}
            temp['imgscr']=m.xpath('./div/a/img/@src').extract_first()
            temp['price'] = m.xpath('./p/em/@title').extract_first()
            temp['shop_name']=m.xpath('./div[3]/a/text()').extract_first()
            temp['sales']=m.xpath('./p[3]/span[1]/em/text()').extract_first()
            if temp['price']==None:
                pass

            else:
                f.write(temp['imgscr'])
                f.write('\n')
                f.write(temp['price'])
                f.write('\n')
                f.write(temp['shop_name'])
                f.write('\n')
                f.write(temp['sales'])
                f.write('\n')


        f.close()




