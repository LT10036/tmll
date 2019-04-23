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

        # 获取传过来的url
        url=request.url

        # 开启浏览器无头模式
        opt = webdriver.ChromeOptions()
        opt.add_argument('--headless')
        opt.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=opt)

        # 隐式等待 最多10秒
        driver.implicitly_wait(10)

        # 开始请求
        driver.get(url)

        # if 判断暂时停用，直接esle执行下边
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
            # 屏幕滚动，完成js 渲染（每次500像素）
            while i<11:

                js='window.scrollTo(0,%d)'%m

                driver.execute_script(js)
                i=i+1
                m=500+m
                time.sleep(3)
        #得到渲染后的页面全部源码
        data=driver.page_source
        # 截个图验证下（无头模式）
        driver.save_screenshot('123.png')

        # 关闭当前浏览器标签
        driver.close()

        # 关闭浏览器
        # driver.quit()

        # 组织响应体
        res=HtmlResponse(url=url,
                         body=data,
                         request=request,
                         encoding='utf-8')


        # 返回响应体
        return res
