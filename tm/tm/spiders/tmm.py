# -*- coding: utf-8 -*-
import scrapy
import re


# 天猫的验证比价有意思。你不能带cookie直接访问，因为设置了cookie是随浏览器关闭而清除掉，重新赋值的，可能涉及到时间戳之类的关键词
# 可以试试调用一个已打开浏览器，之后再打开页面可以从这个里边再添加新窗口


class TmmSpider(scrapy.Spider):
    name = 'tmm'
    allowed_domains = ['tmall.com']

    # 暂时写死只抓取运动鞋类，后续动态输入即可
    start_urls = ['https://list.tmall.com/search_product.htm?q=%D4%CB%B6%AF%D0%AC&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&xl=yundongxi_2&from=mallfp..pc_1_suggest']






    def parse(self, response):

        # 暂时保存到文本文件中，后续再改吧
        f = open('123.txt', 'w')

        # 获取所需要的模块集合
        i=response.xpath('//*[@id="J_ItemList"]/div/div')

        # 开始抓取模块中单个数据
        for m  in i:

            # 空字典接收值
            temp={}

            # 图片地址需要组织头部 "https:"，@src 获取src类链接地址
            temp['imgscr'] = 'https:'+m.xpath('./div/a/img/@src').extract_first()
            temp['price'] = m.xpath('./p/em/@title').extract_first()

            # text() 获取文本内容
            temp['shop_name']=m.xpath('./div[3]/a/text()').extract_first()
            temp['sales']=m.xpath('./p[3]/span[1]/em/text()').extract_first()

            # 模块集合内容有的为空，只能获取图片，写入时会出错，在文本文件中。写入数据库的话，可以直接设置允许为空
            # 以price为例判断内容是否完整，如为空，则跳过写入过程。不为空，则开始写入数据
            if temp['price']==None:
                pass
            #选择后开始写入。为了格式和方便读出，记得写换行
            else:
                f.write(temp['imgscr'])
                f.write('\n')
                f.write(temp['price'])
                f.write('\n')
                f.write(temp['shop_name'])
                f.write('\n')
                f.write(temp['sales'])
                f.write('\n')
                # 新页面打开时因为调用的新的窗口
                # 注意恶心的网址有个无关的参数在里边，去掉后不影响数据采集，不要去管那个参数
                # 遇到个别窗口时显示“店小二正忙，页面打不开。需要拖动一个span到指定位置
                # selenium 有鼠标拖动选项，ActionChains(driver).drag_and_drop_by_offset(source,x轴向素,y轴像素)


        # 文本关闭
        f.close()

        # 暂时不写后续下一页，可以根据地址栏自己组织地址，也可以用“下一页”标签获取链接再请求
        # 初步分析，地址栏从第二页开始有个aq参数，以每页60的相加（没有60，从120开始的）

        # yield scrapy.Request(url='',callback=self.parse())




