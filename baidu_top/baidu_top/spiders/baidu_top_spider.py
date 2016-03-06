# -*- coding:UTF-8 -*-
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from baidu_top.items import BaiduTopItem
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
import sys
import string
sys.stdout=open('output.txt','w')


class BaiduTopSpider(CrawlSpider):
    name = "baidu_top"
    allowed_domains = ["top.baidu.com"]
    start_urls = [
            "http://top.baidu.com/boards?fr=topcategory_c18",
            ]
    rules = (
                Rule(LxmlLinkExtractor(allow=('buzz\?b='), restrict_xpaths=('//html/body/div[@class="wrapper"]/div[@class="main"]/div[@class="all-list"]/div[@class="bd"]/div[@class="links"]/a'), attrs=('href')), callback="parse_item"),
            );
    '''
    rules = (
            Rule(SgmlLinkExtractor(allow=('buzz\?b=', )), callback="parse_item"),
            )
    '''
    def parse_item(self, response):
        ##提取元素
        for link in response.xpath('//html/body/div[@class="wrapper"]/div[@class="main"]/div[@class="all-list"]'):
            top_class = link.xpath('div[@class="hd"]/h3[@class="title"]/a/text()').extract()[1].encode('UTF-8', 'ignore').strip();
            for inner_link in link.xpath('div[@class="bd"]/div[@class="links"]/a'):
                url = inner_link.xpath('@href').extract()[0].encode('UTF-8', 'ignore').strip();
                anchor = inner_link.xpath('text()').extract()[0].encode('UTF-8', 'ignore').strip();
                print top_class + "\thttp://top.baidu.com/" + url + "\t" + anchor;
                #start_urls.append("http://top.baidu.com/" + url)
                
        title = ";".join(response.xpath('/html/head/title/text()').extract()).encode('UTF-8', 'ignore');

        for link in response.xpath('//div[@class="wrapper"]/div[@class="main"]/div[@class="mainBody"]/div[@class="grayborder"]/table[@class="list-table"]/tr/td[@class="keyword"]'):
        #for link in response.xpath('//div/div[@class="wrap c"]/div[@class="main"]/div[@class="mainBody"]/div[@class="mainCon"]/div[@class="list c"]/ul/li'):
            link_anchor = link.xpath('a[@class="list-title"]/text()').extract()[0].encode('UTF-8', 'ignore');
            link_url = link.xpath('a[@class="list-title"]/@href').extract()[0].encode('UTF-8', 'ignore');
            print response.url + "\t" + title + "\t" + link_anchor + "\t" + link_url;
