from lxml import etree
from dataset.data import Data
from strategy.parser.default_parser import DefaultParser
import re
class ListParser(DefaultParser):
    def __init__(self):
        self._page = 1

    def _get_new_data(self, dom):
        new_datas = []
        try:
            # name
            # image
            titles = dom.xpath("//div[@class='box']//h2/a")
            imgs = dom.xpath("//div[@class='box']//a/img[@class='logo img-rounded']")
            details = dom.xpath("//div[@class='box']/a")
            for i in range(0, len(titles)):
                data = Data('ss_stack')
                title =  titles[i].text
                img = imgs[i].get('src')
                detail = details[i].get('href') 
                id = re.search(r'\d+', detail).group()
                detail = 'https://www.sdk.cn' + detail
                data.set('title', title)
                data.set('imgurl', img)
                data.set('detail', detail)
                data.set('refid', id)
                new_datas.append(data)

        except Exception as e:
            print(str(e))
        return new_datas

    def _get_next_page_url(self, dom):
        try:
            next_page_url = dom.xpath("//li[@class='next']/a")
            if len(next_page_url) < 1:
                return None
            return 'https://www.sdk.cn' + next_page_url[0].get('href')
        except Exception as e:
            print(str(e))
            return None
