from lxml import etree
from dataset.data import Data
from strategy.parser.default_parser import DefaultParser
import re
class ListParser(DefaultParser):
    def __init__(self):
        self._page = 1
        self._new_urls = []
    
    def _get_new_urls(self, page_url, dom):
        return self._new_urls

    def _get_new_data(self, dom):
        new_datas = []
        try:
            # company
            nodes = dom.xpath("//a[starts-with(@href, 'http://company.zhaopin.com/CC')]")
            if nodes is None:
                return new_datas
            for node in nodes:
                d = Data('ss_company')
                d.set('name', node.text)
                d.set('refid', re.search(r'\d+', node.get('href')).group())
                url = node.get('href')
                d.set('url', url)
                if d in new_datas:
                    continue
                else:
                    self._new_urls.append(url) # append the url
                    new_datas.append(d)
            # jobs
            nodes = dom.xpath("//a[starts-with(@href, 'http://jobs.zhaopin.com/')]")
            for node in nodes:
                url = node.get('href')
                self._new_urls.append(url) # append the jobs url
        except Exception as e:
            print(str(e))
        return new_datas

    def _get_next_page_url(self, dom):
        next_page_url = dom.xpath("//a[@class='next-page']/@href")
        if len(next_page_url) < 1:
            return None
        return next_page_url[0]
