# -*- coding: utf-8 -*-
from lxml import etree
from dataset.data import Data
from strategy.parser.default_parser import DefaultParser
import re
class JobParser(DefaultParser):
    def _get_new_data(self, dom):
        try:
            # get title
            nodes = dom.xpath("//div[@class='top-fixed-box']//h1")
            if len(nodes) < 1:
                return None
            title = nodes[0].text
            if title is None:
                return None
            # get company
            nodes = dom.xpath("//div[@class='top-fixed-box']//h2/a")
            if len(nodes) < 1:
                return None
            company = nodes[0].text

            # get scale
            nodes = dom.xpath("//div[@class='terminalpage']//ul[@class='terminal-ul']/li[1]/strong")
            if len(nodes) < 1:
                return None
            scale = nodes[0].text

            # get detail
            nodes = dom.xpath("//div[@class='tab-inner-cont']")
            detail = self._get_children_text(nodes)

            # get id
            nodes = dom.xpath("//link[@rel='canonical']/@href")
            if len(nodes) < 1:
                return None
            url = nodes[0]
            id = re.search(r'\d+', url).group()

            data = Data('ss_job')
            data.set('title', title)
            data.set('company', company)
            data.set('scale', scale)
            data.set('detail', detail)
            data.set('id', id)
            return [data]

        except Exception as e:
            print(str(e))
            return None
