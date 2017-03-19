# -*- coding: utf-8 -*-
# main function
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from spider.base_spider import BaseSpider

if __name__ == '__main__':
    spider = BaseSpider()
    spider.set_domain('zhaopin.com')
    spider.set_entry('http://sou.zhaopin.com/jobs/searchresult.ashx?bj=160000&in=210500%3B160400%3B160000%3B160200%3B160600&jl=%E6%89%AC%E5%B7%9E&p=1&isadv=0')
    spider.run()