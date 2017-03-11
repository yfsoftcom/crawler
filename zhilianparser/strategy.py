import re
from list_parser import ListParser
from company_parser import CompanyParser
from unknown_parser import UnknownParser
class Strategy(object):
  def __init__(self):
    pass

  def get_strategy(self, url):
    if re.match(r'^http://sou.zhaopin.com/jobs/searchresult.ashx', url) != None:
      return ListParser()
    if re.match(r'^http://company.zhaopin.com/', url) != None:
      return CompanyParser()
    return UnknownParser()