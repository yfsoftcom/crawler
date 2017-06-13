from lxml import etree
import json
from dataset.data import Data
from downloader.downloader import Downloader
import re
downloader = Downloader()

ai = { u'counter': 0}

class DefaultAutoSpiderParser(object):
    def __init__(self, spider, is_html = True, data = None):
        self._spider = spider
        self._page = 1
        self.is_html = is_html
        self._url = None
        self._data = data
      
    def _get_new_urls(self, page_url, dom):
        if 'prefix' in self._spider._range.keys():
            return dom.xpath(self._spider._range['prefix'] + '//a[@href]/@href')
        return dom.xpath('//a[@href]/@href')

    def _get_new_data(self, dom):
        data = Data(self._spider._id)
        data.set('refurl' , self._url)
        for field in self._spider._fields:
            value = self.get_value(field, dom)
            data.set(field['name'], value)
        return [ data ]

    def get_value(self, field, dom):
        if field['type'] == 'ai':
            ai['counter'] = ai['counter'] + 1
            return ai['counter']

        node = dom.xpath(field['xpath'])
        if field['type'] == 'string':
            if len(node) > 0:
                value = node[0]
            if 'filter' in field.keys():
                m = re.compile(field['filter']).search(value)
                if m != None:
                    value = m.group(0)
            return value
        
        if field['type'] == 'xml':
            if len(node) > 0:
                value = node[0]
            value = etree.tostring(value, encoding='utf8')
            value = self._remove_white_space(value)
            return value


    def parse(self, url, type = 'CONTENT'):
        self._url = url
        html = downloader.download(url)
        if self.is_html:
            dom = etree.HTML(html)
        else:
            dom = json.loads(html)

        if type is 'CONTENT':
            data = self._get_new_data(dom)
            urls = None
        else:
            data = None
            urls = self._get_new_urls(url, dom)
        return urls, data

    def _get_children_text(self, nodes):
        if len(nodes) < 1:
            return None
        return self._remove_white_space(nodes[0].xpath('string(.)'))

    def _remove_white_space(self, text):
        text = re.sub(r'\s{2,}', '', text)
        return text

    def _filter(self, datas):
        return datas



    