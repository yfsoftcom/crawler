import re

from company_list_parser import ListParser
from company_parser import CompanyParser
from job_parser import JobParser
from strategy.parser.unknown_parser import UnknownParser
from strategy.strategy import Strategy

class ZhaoPinStrategy(Strategy):
  def __init__(self):
    pass

  def get_parser(self, url):
    if re.match(r'^http://sou.zhaopin.com/jobs/searchresult.ashx', url) != None:
      return ListParser()
    if re.match(r'^http://company.zhaopin.com/', url) != None:
      return CompanyParser()
    if re.match(r'^http://jobs.zhaopin.com/', url) != None:
      return JobParser()
    return UnknownParser()

  def _filter(self, input):
    return 'addr' in input.keys()
