﻿# -*- coding: utf-8 -*-
from lxml import etree
from dataset.data import Data
from strategy.parser.default_parser import DefaultParser
import re
class CompanyParser(DefaultParser):
    def _get_new_data(self, dom):
        try:
            # get addr
            nodes = dom.xpath("//span[@class='comAddress']")
            if len(nodes) < 1:
                return None
            addr = nodes[0].text
            if addr is None:
                return None
            data = Data('ss_company')
            data.set('addr', addr)

            # get detail
            nodes = dom.xpath("//div[@class='company-content']")
            detail = self._get_children_text(nodes)
            if detail is None:
                return None
            data.set('detail', detail)

            # get id
            nodes = dom.xpath("//link[@rel='canonical']/@href")
            if len(nodes) < 1:
                return None
            url = nodes[0]
            id = re.search(r'\d+', url).group()
            data.set('refid', id)
        except Exception as e:
            print(str(e))
        return [data]
