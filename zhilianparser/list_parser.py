from lxml import etree
from dataset.data import Data
from default_parser import DefaultParser
import re
class ListParser(DefaultParser):
    def __init__(self):
        self._page = 1

    def _get_new_data(self, dom):
        new_datas = []
        try:
            nodes = dom.xpath("//a[starts-with(@href, 'http://company.zhaopin.com/CC')]")
            if nodes is None:
                return new_datas
            for node in nodes:
                d = Data()
                d.set('name', node.text)
                d.set('id', re.search(r'\d+', node.get('href')).group())
                d.set('url', node.get('href'))
                if d in new_datas:
                    continue
                else:
                    new_datas.append(d)
        except Exception as e:
            print(str(e))
        return new_datas

    def _get_next_page_url(self, dom):
        next_page_url = dom.xpath("//a[@class='next-page']/@href")
        if len(next_page_url) < 1:
            return None
        return next_page_url[0]

    def parse(self, url, html):
        dom = etree.HTML(html)
        return self._get_new_urls(url, dom), self._get_new_data(dom), self._get_next_page_url(dom)