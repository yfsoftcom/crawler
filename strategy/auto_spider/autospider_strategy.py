import re

from strategy.strategy import Strategy
from strategy.parser.unknown_parser import UnknownParser
from strategy.parser.autospider_parser import DefaultAutoSpiderParser

class AutoSpiderStrategy(Strategy):
  def __init__(self, spider = None):
    self._spider = spider

  def get_parser(self, url, is_html = True, data = None, encoding = 'utf-8'):
    # print url
    
    return DefaultAutoSpiderParser(self._spider, encoding = encoding)

  def _filter(self, input):
    return True
