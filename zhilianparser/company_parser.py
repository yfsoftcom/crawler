from lxml import etree
from dataset.data import Data
from default_parser import DefaultParser
import re
class CompanyParser(DefaultParser):

    def _get_new_data(self, dom):
        data = Data()
        try:
            url = dom.xpath("//link[@rel='canonical']/@href")
            if url is None:
                return data
            url = url[0]
            id = re.search(r'\d+', url).group()
            data.set('id', id)
            addr = dom.xpath("//span[@class='comAddress']")
            if len(addr) > 0:
                addr = addr[0].text
                if addr != None:
                        addr = re.sub(r'\(', ' ', addr )
                        addr = re.sub(r'\)', ' ', addr )
                        addr = re.sub(r'\s{2,}', ',', addr )
                        data.set('addr', addr)
        except Exception as e:
            print(str(e))
        return data