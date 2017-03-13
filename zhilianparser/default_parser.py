from lxml import etree
from dataset.data import Data
import re
class DefaultParser(object):
    def __init__(self):
        self._page = 1
    
    def _get_new_urls(self, page_url, dom):
        return None

    def _get_new_data(self, dom):
        return None

    def _get_next_page_url(self, dom):
        return None

    def parse(self, url, html):
        dom = etree.HTML(html)
        data = self._get_new_data(dom)
        urls = self._get_new_urls(url, dom)
        next_page = self._get_next_page_url(dom)
        return urls, data, next_page

    def _get_children_text(self, nodes):
        text = ''
        for node in nodes:
            if isinstance(node, etree._ElementUnicodeResult):
                text = text + node
        return text

    