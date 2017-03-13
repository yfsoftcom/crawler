# -*- coding: utf-8 -*-
from lxml import etree
from dataset.data import Data
from default_parser import DefaultParser
import re
class CompanyParser(DefaultParser):
    def _get_new_data(self, dom):
        try:
            addr = dom.xpath("//span[@class='comAddress']")
            if len(addr) < 1:
                return None
            addr = addr[0].text
            if addr is None:
                return None
            data = Data()
            # addr = re.sub(r'\(', ' ', addr )
            # addr = re.sub(r'\)', ' ', addr )
            # addr = re.sub(r'\s{2,}', ',', addr )
            # print addr
            data.set('addr', addr)

            url = dom.xpath("//link[@rel='canonical']/@href")
            if url is None:
                return None
            url = url[0]
            id = re.search(r'\d+', url).group()
            data.set('id', id)
        except Exception as e:
            print(str(e))
        return data