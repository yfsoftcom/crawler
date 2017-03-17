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
        self.urls = list()

    def start_urls(self, urls):
        if isinstance(urls, list):
            for url in urls:
                self.urls.append(url)
        else:
            self.urls.append(urls)

    def data_validate(self):
        row = self.dataset.get_list()
        row = self.strategy.validate(row)
        return row
    
    def output_data(self, row):
        print '###### datas start#####'
        print row
        print '###### datas end #####'

    def upload_data(self, row):
        return self.fpm_lib.call_func('common.create', {'table': 'ss_company', 'row': row})

    def run(self):
        for url in self.urls:
            print 'run start with %s' % (url)
            self.url_manager.add(url)
            while self.url_manager.has_next():
                try:
                    url = self.url_manager.next()
                    html = self.downloader.download(url)
                    parser = self.strategy.get_strategy(url)
                    new_urls, data, next_page_url = parser.parse(url, html)
                    self.url_manager.add(next_page_url)
                    self.url_manager.add_all(new_urls)
                    # filter data
                    data = parser._filter(data)
                    self.dataset.insert(data)
                    if(self.counter > 100):
                        break
                    self.counter = self.counter + 1

                except Exception as e:
                    print(str(e))

            row = self.data_validate()
            self.output_data(row)
            # self.upload_data(row)