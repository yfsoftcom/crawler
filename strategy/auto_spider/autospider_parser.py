from lxml import etree
from dataset.data import Data
from strategy.parser.default_parser import DefaultParser
import re
class AutoSpiderParser(DefaultParser):
    def __init__(self):
        self._page = 1



    def parse(self, url):
        self._url = url
        html = downloader.download(url)
        if self.is_html:
            dom = etree.HTML(html)
        else:
            dom = json.loads(html)
            
        data = self._get_new_data(dom)
        urls = self._get_new_urls(url, dom)
        return urls, data, []    

    def get_allowed_partten(self, dom, allowed_partten):
      a_nodes = dom.xpath('//a[@href]/@href')
      if len(a_nodes) < 1:
          return []
      else:
          print (a_nodes)
          allowed_urls = []
          for node in a_nodes:
              if re.match(allowed_partten, node) != None:
                  allowed_urls.append(node)

          return allowed_urls