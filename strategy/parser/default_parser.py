from lxml import etree
import json
from dataset.data import Data
from downloader.downloader import Downloader
import re

downloader = Downloader()

class DefaultParser(object):
    def __init__(self, is_html = True):
        self._page = 1
        self.is_html = is_html
        self._url = None
    
    def _get_new_urls(self, page_url, dom):
        return None

    def _get_new_data(self, dom):
        return None

    def _get_next_page_url(self, dom):
        return None

    def parse(self, url):
        self._url = url
        html = downloader.download(url)
        if self.is_html:
            dom = etree.HTML(html)
        else:
            dom = json.loads(html)
        data = self._get_new_data(dom)
        urls = self._get_new_urls(url, dom)
        next_page = self._get_next_page_url(dom)
        return urls, data, next_page

    def _get_children_text(self, nodes):
        if len(nodes) < 1:
            return None
        return self._remove_white_space(nodes[0].xpath('string(.)'))

    def _remove_white_space(self, text):
        text = re.sub(r'\s{2,}', '', text)
        return text

    def _filter(self, datas):
        return datas
    