from lxml import etree
from dataset.data import Data
from strategy.parser.default_parser import DefaultParser
import re
class ModelParser(DefaultParser):
    def __init__(self):
        self._page = 1
        self.is_html = False

    def _get_new_data(self, dom):
        new_datas = []
        try:
            datas = dom['result']['yearitems']
            for d in datas:
                data = Data('year')
                data.set('id', d['id'])
                data.set('name', d['name'])
                new_datas.append(data)
                spec = d['specitems']
                for sub_d in spec:
                    sub_data = Data('spec', sub_d)
                    new_datas.append(sub_data)
                
        except Exception as e:
            print(str(e))
        return new_datas

    def _get_next_page_url(self, dom):
        pass
