import selenium
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time

opt=webdriver.ChromeOptions()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
driver=webdriver.Chrome(chrome_options=opt)
driver.implicitly_wait(10)
url='https://tmall.com'
driver.get(url)
if url=='https://tmall.com':
    m=input('请输入：')
    driver.find_element_by_xpath('//*[@id="mq"]').send_keys(m)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="mallSearch"]/form/fieldset/div/button').click()
    time.sleep(3)
else:
    pass
driver.save_screenshot('1231.png')
driver.quit()




# import scrapy
# import json
#
# ls=[]
#
#
# n = input('请输入关键词：')
#
#
# class TbSpider(scrapy.Spider):
#     name = 'tb'
#     allowed_domains = ['tieba.baidu.com']
#     start_urls = ['https://tieba.baidu.com/f?kw=吐槽']
#
#
#
#
#
#     def parse(self, response):
#         global ls
#         global n
#
#         list_scr=response.xpath('//*[@id="thread_list"]/li/div/div[2]/div')
#
#
#         print(len(list_scr))
#
#
#         for i in list_scr:
#
#             temp={}
#             temp['title']=i.xpath('./div/a/text()')
#             # temp['auth']=i.xpath('./div/span/span/a/text()')
#             # temp['href'] = i.xpath('./div/a/@href)')
#             if temp['title']==[]:
#                 pass
#             else:
#                # temp['title'] = i.xpath('./div/a/text()')[0].extract()
#                # temp['auth'] = i.xpath('./div/span/span/a/text()')[0].extract()
#                temp['title'] = i.xpath('./div/a/text()')[0].extract()
#                temp['href'] = response.urljoin(i.xpath('./div/a/@href').extract_first())
#
#                # 跟 据 输 入 的 条 件 搜 索 每 一 页 数 据， 如 果 符 合 就 写 入 文 件
#                if n in (temp['title'] or temp['auth']):
#                     # f.write(str(temp))
#                     # f.write('\n')
#                     ls.append(temp)
#                else:
#                    pass
#         for i in range(1,455):
#             url='https://tieba.baidu.com/f?kw=%E5%90%90%E6%A7%BD&ie=utf-8&pn='+str(i*50)
#
#             yield scrapy.Request(url, callback=self.parse)
#         print(len(ls))
#         print(ls)
#         f = open('123.txt', 'w')
#         for i in ls:
#
#             f.write('标题:'+i['title'])
#             f.write('\n')
#             f.write('链接：'+i['href'])
#             f.write('\n')
#         f.close()