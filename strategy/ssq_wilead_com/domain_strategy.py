import re

from list_parser import ListParser
from post_parser import PostParser
from strategy.parser.unknown_parser import UnknownParser
from strategy.strategy import Strategy

class ComWileadSsqStrategy(Strategy):
  def __init__(self):
    pass

  def get_parser(self, url):
    print url
    if re.match(r'^http://ssq.wilead.com/user/\d*.html', url) != None:
      print 'list'
      return ListParser()
    if re.match(r'^http://ssq.wilead.com/post/\d*.html', url) != None:
      return PostParser()
    return UnknownParser()

  def _filter(self, input):
    return True
