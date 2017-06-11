from lxml import etree
import json
from dataset.data import Data
from downloader.downloader import Downloader
import re

downloader = Downloader()

class DefaultAutoSpiderParser(object):
    def __init__(self, is_html = True, data = None):
        self._page = 1
        self.is_html = is_html
        self._url = None
        self._data = data
    
    def set_fields(self, fields):
        self.fields = fields

    def set_allowed_partten(self, allowed_partten):
        self.allowed_partten = allowed_partten
    
    def set_content_url_partten(self, content_url_partten):
        self.content_url_partten = content_url_partten

    def set_list_url_partten(self, list_url_partten):
        self.list_url_partten = list_url_partten

    def get_allowed_partten(self, dom):
      a_nodes = dom.xpath('//a[@href]/@href')
      if len(a_nodes) < 1:
          return []
      else:
          allowed_urls = []
          for node in a_nodes:
              if re.match(r'^/', node) != None:
                  node = self._domain + node
              allowed_urls.append(node)
          return allowed_urls
          
    def get_domain(self):
        return re.search(r'^((http://)|(https://))?([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}(/)', self._url).group()[0:-1]

    def _get_new_urls(self, page_url, dom):

        return self.get_allowed_partten(dom)

    def _get_new_data(self, dom):
        for field in self.fields:
            node = dom.xpath(field.xpath)
            print node
        return None

    def _get_next_page_url(self, dom):
        return None

    def parse(self, url):
        self._url = url
        self._domain = self.get_domain()
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



    