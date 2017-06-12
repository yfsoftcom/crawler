import re

from strategy.strategy import Strategy
from strategy.parser.unknown_parser import UnknownParser
from strategy.parser.autospider_parser import DefaultAutoSpiderParser

class AutoSpiderStrategy(Strategy):
  def __init__(self):
    pass

  def get_parser(self, url):
    # print url
    
    return DefaultAutoSpiderParser()

  def _filter(self, input):
    return True
