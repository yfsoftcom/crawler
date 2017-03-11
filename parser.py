from lxml import etree
import data
class SimpleParser(object):
    def __init__(self):
        self._page = 1
    
    def _get_new_urls(self, page_url, dom):
        new_urls = set()
        try:
            nodes = dom.xpath("//a[starts-with(@href, 'http://company.zhaopin.com/CC')]/@href")
            if nodes is None:
                return new_datas
            for node in nodes:
                if node in new_urls:
                    continue
                else:
                    new_urls.add(node)
        except Exception as e:
            print(str(e))
        return new_urls

    def _get_new_data(self, dom):
        new_datas = set()
        try:
            nodes = dom.xpath("//a[starts-with(@href, 'http://company.zhaopin.com/CC')]")
            if nodes is None:
                return new_datas
            for node in nodes:
                d = data.Data()
                d.set('name', node.text)
                d.set('id', node.text)
                d.set('url', node.get('href'))
                if d in new_datas:
                    continue
                else:
                    new_datas.add(d)
        except Exception as e:
            print(str(e))
        return new_datas

    def _get_next_page_url(self, dom):
        return None

    def parse(self, url, html):
        dom = etree.HTML(html)
        return self._get_new_urls(url, dom), self._get_new_data(dom)