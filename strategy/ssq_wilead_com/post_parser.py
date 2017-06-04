from lxml import etree
from dataset.data import Data
from strategy.parser.default_parser import DefaultParser
import re
class PostParser(DefaultParser):
    def __init__(self):
        self.super = super(PostParser, self)
        self.super.__init__()

    def get_url_value(self):
        v = re.search(r'\d*.html$', self._url).group()
        return int(re.search(r'^\d*', v).group())

    def clear_space(self, content):
        # r, n = re.subn(r'>\\n\s*<', '><', content)
        r = re.compile(r'\n\s*')
        return r.sub('', content)

    def _get_new_data(self, dom):
        new_datas = []
        try:
            nodes = dom.xpath("//article//h1//a/text()")
            if len(nodes) < 1:
                return None
            author = nodes[0].encode('utf8')

            nodes = dom.xpath("//article//h1/text()")
            if len(nodes) < 1:
                return None
            title = nodes[1].encode('utf8')

            content = ''
            nodes = dom.xpath("//article//section")
            for node in nodes:
                content = content + etree.tostring(node, encoding='utf8')
            data = Data('post')
            data.set('title', title)
            data.set('author', self.clear_space(author))
            data.set('content', self.clear_space(content))
            data.set('id', self.get_url_value())
            new_datas.append(data)

        except Exception as e:
            print(str(e))
        return new_datas

    def _get_next_page_url(self, dom):
        return None
