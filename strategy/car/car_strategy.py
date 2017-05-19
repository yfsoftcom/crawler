import re

from brand_parser import BrandParser
from series_parser import SeriesParser
from model_parser import ModelParser
from strategy.parser.unknown_parser import UnknownParser
from strategy.strategy import Strategy

class CarStrategy(Strategy):
  def __init__(self):
    pass

  def get_parser(self, url):
    print url
    if re.match(r'^http://www.autohome.com.cn/ashx/AjaxIndexCarFind.ashx\?type=1', url) != None:
      return BrandParser()

    if re.match(r'^http://www.autohome.com.cn/ashx/AjaxIndexCarFind.ashx\?type=3', url) != None:
      return SeriesParser()

    if re.match(r'^http://www.autohome.com.cn/ashx/AjaxIndexCarFind.ashx\?type=5', url) != None:
      return ModelParser()

    return UnknownParser()

  def _filter(self, input):
    return True
