# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time

from scrapy import signals
from selenium import webdriver

from scrapy.http import HtmlResponse

class opennew(object):
    def process_request(self, request, spider):

        url=request.url
        opt = webdriver.ChromeOptions()
        opt.add_argument('--headless')
        opt.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=opt)
        driver.implicitly_wait(10)
        driver.get(url)
        if url == 'https://tmall.com':
            # m = input('请输入：')
            driver.find_element_by_xpath('//*[@id="mq"]').send_keys('运动鞋')
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="mallSearch"]/form/fieldset/div/button').click()
            time.sleep(3)
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            data = driver.page_source
            driver.close()
        else:
            time.sleep(5)
            i=0
            m=500
            while i<11:

                js='window.scrollTo(0,%d)'%m

                driver.execute_script(js)
                i=i+1
                m=500+m
                time.sleep(3)

        data=driver.page_source
        driver.save_screenshot('123.png')

        driver.close()
        res=HtmlResponse(url=url,
                         body=data,
                         request=request,
                         encoding='utf-8')



        return res
