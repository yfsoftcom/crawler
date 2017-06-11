# -*- coding: utf-8 -*-

from url_manager.url_manager import UrlManager
from strategy.auto_spider.autospider_strategy import AutoSpiderStrategy
from dataset.dataset import Dataset
class AutoSpider(object):

  def __init__(self):
    # 构造一些工具，dataset，urlmanager , strategy paser
    self.url_manager = UrlManager()
    self.dataset = Dataset()
  
  def set_domain(self, domain, allowed_partten = None):
    self.url_manager.set_domain(domain, allowed_partten)
    self.strategy = AutoSpiderStrategy()

  def set_entry(self, entry):
    self.url_manager.get_manager().add(entry)

  def set_list_url_partten(self, partten):
    self.partten_list_url = partten

  def set_content_url_partten(self, partten):
    self.partten_content_url = partten

  def run(self):
    # 解析里面所有被允许的a标签
    print ('autospider run')
    url_mgr = self.url_manager.get_manager()
    counter = 0
    while url_mgr.has_next():
      url = url_mgr.next()
      parser = self.strategy.get_parser(url)
      try:
        new_urls, new_datas, next_page = parser.parse(url)
        url_mgr.add_all(new_urls)
        print new_urls, new_datas, next_page

        if counter > 10: 
          break
        counter = counter + 1
      except Exception as e:
        print(str(e))
        continue
    
    #self.dataset.output()
    
    