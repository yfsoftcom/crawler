from lxml import etree
from dataset.data import Data
from strategy.parser.default_parser import DefaultParser
import re
class ListParser(DefaultParser):
    def __init__(self):
        self.super = super(ListParser, self)
        self.super.__init__()
        self._new_urls = []
    
    def _get_new_urls(self, page_url, dom):
        return self._new_urls

    def _get_new_data(self, dom):
        new_datas = []
        try:
            hrefs = dom.xpath("//article//a/@href")
            for href in hrefs:
                self._new_urls.append('http://ssq.wilead.com' + href)
        except Exception as e:
            print(str(e))
        return new_datas

    def _get_next_page_url(self, dom):
        return None
