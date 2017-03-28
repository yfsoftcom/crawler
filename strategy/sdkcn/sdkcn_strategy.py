import re

from lan_framework_list_parser import ListParser
from strategy.parser.unknown_parser import UnknownParser
from strategy.strategy import Strategy

class SdkcnStrategy(Strategy):
  def __init__(self):
    pass

  def get_parser(self, url):
    print url
    if re.match(r'^https://www.sdk.cn/datas\?category_id=100100', url) != None:
      return ListParser()

    return UnknownParser()

  def _filter(self, input):
    return True
