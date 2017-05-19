from strategy.parser.default_parser import DefaultParser
import re
class CarParser(DefaultParser):
    def __init__(self):
        self._page = 1
        self.is_html = False

    def get_url_value(self):
        v = re.search(r'value=\d*', self._url).group()
        return int(re.search(r'\d*$', v).group())
