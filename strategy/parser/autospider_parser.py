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
          
    def _get_new_urls(self, page_url, dom):
        return dom.xpath('//a[@href]/@href')

    def _get_new_data(self, dom):
        # if content page
        # try:
        #     # name
        #     # image
        #     titles = dom.xpath("//div[@class='box']//h2/a")
        #     imgs = dom.xpath("//div[@class='box']//a/img[@class='logo img-rounded']")
        #     details = dom.xpath("//div[@class='box']/a")
        #     for i in range(0, len(titles)):
        #         data = Data('ss_stack')
        #         title =  titles[i].text
        #         img = imgs[i].get('src')
        #         detail = details[i].get('href') 
        #         id = re.search(r'\d+', detail).group()
        #         detail = 'https://www.sdk.cn' + detail
        #         data.set('title', title)
        #         data.set('imgurl', img)
        #         data.set('detail', detail)
        #         data.set('refid', id)
        #         new_datas.append(data)
        # except Exception as e:
        #     print(str(e))
        # return new_datas
        data = Data('auto')
        for field in self.fields:
            node = dom.xpath(field['xpath'])
            if len(node) > 0:
                node = node[0]
            if 'filter' in field.keys():
                m = re.compile(field['filter']).search(node)
                if m != None:
                    node = m.group(0)
            data.set(field['name'], node)
        return [ data ]

    def parse(self, url, type = 'CONTENT'):
        self._url = url
        html = downloader.download(url)
        # print html
        if self.is_html:
            dom = etree.HTML(html)
        else:
            dom = json.loads(html)
        if type is 'CONTENT':
            data = self._get_new_data(dom)
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



    