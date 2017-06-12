# -*- coding: utf-8 -*-
# main function
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import re
from spider.base_spider import BaseSpider
from spider.auto_spider import AutoSpider

if __name__ == '__main__':
    # spider = BaseSpider()

    # zhaopin.com
    # spider.set_domain('zhaopin.com')
    # spider.set_entry('http://sou.zhaopin.com/jobs/searchresult.ashx?bj=160000&in=210500%3B160400%3B160000%3B160200%3B160600&jl=%E6%89%AC%E5%B7%9E&p=1&isadv=0')
    # spider.run()

    # sdk.cn
    
    # spider.set_domain('sdk.cn')
    # spider.set_entry('https://www.sdk.cn/datas?category_id=100100')
    # spider.run()

    # autohome.com.cn

    # spider.set_domain('www.autohome.com.cn')
    # spider.set_entry('http://www.autohome.com.cn/ashx/AjaxIndexCarFind.ashx?type=1')
    # spider.run()

    # ssq.wilead.com
    # spider.set_domain('ssq.wilead.com')
    # spider.set_entry('http://ssq.wilead.com/user/16.html')
    # spider.run()


    # spider = AutoSpider()

    # spider.set_domain('https://sdk.cn', '^https://sdk.cn/datas\?category_id=100100')
    
    # # spider.set_list_url_partten('')

    # spider.set_content_url_partten('^https://sdk.cn/datas/\d+')

    # spider.set_fields([
    #     { 'name': 'title', 'xpath': '//*[@id="data-view"]/header/div[1]/div[2]/h1/text()' },
    #     { 'name': 'id', 'xpath': '//*[@id="relation-0"]/@target_id' }
    # ])

    # spider.set_entry('https://sdk.cn/datas?category_id=100100')

    # spider.run()


#
    spider = AutoSpider()

    spider.set_domain('http://sou.zhaopin.com', '^http://sou.zhaopin.com/jobs/searchresult.ashx')
    
    # spider.set_list_url_partten('')

    spider.set_content_url_partten('^http://jobs.zhaopin.com/\d+.htm')

    spider.set_fields([
        { 'name': 'title', 'xpath': '/html/body/div[5]/div[1]/div[1]/h1/text()' },
        { 'name': 'company', 'xpath': '/html/body/div[5]/div[1]/div[1]/h2/a/text()' },
        { 'name': 'id', 'xpath': '/html/head/link[@rel="canonical"]/@href', 'filter': '\d+' },
        { 'name': 'refurl', 'xpath': '/html/head/link[@rel="canonical"]/@href' },
    ])

    spider.set_entry('http://sou.zhaopin.com/jobs/searchresult.ashx?bj=160000&in=210500%3B160400%3B160000%3B300100%3B160100%3B160600&jl=%E6%89%AC%E5%B7%9E&p=1&isadv=0')
    spider.run()
