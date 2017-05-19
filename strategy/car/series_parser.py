from lxml import etree
from dataset.data import Data
from strategy.parser.default_parser import DefaultParser
import re
class SeriesParser(DefaultParser):
    def __init__(self):
        self._page = 1
        self.is_html = False
        self._new_urls = []

    def _get_new_data(self, dom):
        new_datas = []
        try:
            datas = dom['result']['factoryitems']
            for d in datas:
                data = Data('series')
                data.set('id', d['id'])
                data.set('name', d['name'])
                data.set('firstletter', d['firstletter'])
                new_datas.append(data)
                sub_datas = d['seriesitems']
                for sub_d in sub_datas:
                    sub_data = Data('sub_series', sub_d)
                    new_datas.append(sub_data)
                    self._new_urls.append('http://www.autohome.com.cn/ashx/AjaxIndexCarFind.ashx?type=5&value=' + str(sub_d['id']))
        except Exception as e:
            print(str(e))
        return new_datas

    def _get_new_urls(self, page_url, dom):
        return self._new_urls

    def _get_next_page_url(self, dom):
        pass
