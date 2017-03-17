# -*- coding: utf-8 -*-
# main function
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from spider.default_spider import Spider

if __name__ == '__main__':
    spider = Spider()
    spider.start_urls('http://sou.zhaopin.com/jobs/searchresult.ashx?bj=160000&in=210500%3B160400%3B160000%3B160200%3B160600&jl=%E6%89%AC%E5%B7%9E&p=1&isadv=0')

    spider.run()