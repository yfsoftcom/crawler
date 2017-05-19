# -*- coding: utf-8 -*-

from url_manager.url_manager import UrlManager
from strategy.strategy_manager import StrategyManager
from dataset.dataset import Dataset
class BaseSpider(object):

  def __init__(self):
    # 构造一些工具，dataset，urlmanager , strategy paser
    self.url_manager = UrlManager()
    self.dataset = Dataset()
    self.strategy_manager = StrategyManager()
  
  def set_domain(self, domain):
    self.url_manager.set_domain(domain)
    self.strategy = self.strategy_manager.get_strategy(domain)

  def set_entry(self, entry):
    self.url_manager.get_manager().add(entry)

  def run(self):
    url_mgr = self.url_manager.get_manager()
    counter = 0
    while url_mgr.has_next():
      url = url_mgr.next()
      parser = self.strategy.get_parser(url)
      try:
        new_urls, new_datas, next_page = parser.parse(url)
        url_mgr.add(next_page)
        url_mgr.add_all(new_urls)
        self.dataset.add_all(new_datas)

        if counter > 5000: 
          break
        counter = counter + 1
      except Exception as e:
        print(str(e))
        continue
    
    self.dataset.output()
    self.dataset.store()
    # self.dataset.sync_fpm()