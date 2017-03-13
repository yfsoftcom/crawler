# -*- coding: utf-8 -*-
# main function
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  

from dataset.dataset import Dataset
from downloader.downloader import Downloader
from zhilianparser.strategy import Strategy
from url_manager.url_manager import UrlManager
from fpm_lib.fpm_lib import FpmLib
class Spider(object):
    def __init__(self):
        self.url_manager = UrlManager()
        self.downloader = Downloader()
        self.strategy = Strategy()
        self.dataset = Dataset()
        self.fpm_lib = FpmLib()
        self.counter = 0

    def run(self, root):
        print 'run root %s' % (root)
        self.url_manager.add(root)
        while self.url_manager.has_next():
            try:
                url = self.url_manager.next()
                html = self.downloader.download(url)
                parser = self.strategy.get_strategy(url)
                new_urls, data, next_page_url = parser.parse(url, html)
                self.url_manager.add(next_page_url)
                self.url_manager.add_all(new_urls)
                self.dataset.insert(data)
                if(self.counter > 100):
                    break
                self.counter = self.counter + 1

            except Exception as e:
                print(str(e))
        
        # self.dataset.store()
        # print self.dataset.get_json()
        # print self.dataset.get_list()
        print self.fpm_lib.call_func('common.create', {'table': 'ss_company', 'row': self.dataset.get_list()})
        # print self.fpm_lib.call_func('system.show', {'table':'123'})

if __name__ == '__main__':
    spider = Spider()
    spider.run('http://sou.zhaopin.com/jobs/searchresult.ashx?bj=160000&in=210500%3B160400%3B160000%3B160200%3B160600&jl=%E6%89%AC%E5%B7%9E&p=1&isadv=0')
    # spider.run('http://company.zhaopin.com/CC435961783.htm')