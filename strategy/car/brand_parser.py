from lxml import etree
from dataset.data import Data
from strategy.parser.default_parser import DefaultParser
import re
class BrandParser(DefaultParser):
    def __init__(self):
        self._page = 1
        self.is_html = False

    def _get_new_data(self, dom):
        new_datas = []
        try:
            datas = dom['result']['branditems']
            for d in datas:
                data = Data('brand', d)
                new_datas.append(data)
        except Exception as e:
            print(str(e))
        return new_datas

    def _get_new_urls(self, page_url, dom):
        new_urls = []
        new_datas = dom['result']['branditems']
        try:
            for item in new_datas:
                new_urls.append('http://www.autohome.com.cn/ashx/AjaxIndexCarFind.ashx?type=3&value=' + str(item['id']))
        except Exception as e:
            print(str(e))
        return new_urls
