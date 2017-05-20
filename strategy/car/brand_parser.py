from lxml import etree
from dataset.data import Data
from strategy.car.car_parser import CarParser
from strategy.parser.default_parser import DefaultParser
import re
class BrandParser(CarParser):
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
                new_urls.append("http://car.autohome.com.cn/price/brand-%d.html" % int(item['id']))
        except Exception as e:
            print(str(e))
        return new_urls

########
#  brand
#  {"bfirstletter": "D", "id": 1, "name": "auto"},
#
########

import re
class LogoParser(DefaultParser):

    def _get_new_data(self, dom):
        new_datas = []
        try:
            src = dom.xpath("//div[@class='carbradn-pic']/img/@src")[0]
            data = Data('brand')
            data.set('refid', self._data)
            data.set('logo', src)
            new_datas.append(data)
        except Exception as e:
            print(str(e))
        return new_datas
