# -*- coding: utf-8 -*-

from url_manager.url_manager import UrlManager
from strategy.auto_spider.autospider_strategy import AutoSpiderStrategy
from dataset.dataset import Dataset
class AutoSpider(object):

  def __init__(self):
    # 构造一些工具，dataset，urlmanager , strategy paser
    self.url_manager = UrlManager()
    self.dataset = Dataset()
    self._allowed_partten = {}
    self._range = {}
    self._id = 'default'
    self._max = 100
    self._encoding = 'utf-8'
  
  def set_max(self, max):
    self._max = int(max)

  def set_id(self, id):
    self._id = id

  def set_domain(self, domain, allowed_partten = None):
    self._domain = domain
    if allowed_partten != None:
      self._allowed_partten['ALLOWED'] = allowed_partten
    self.strategy = AutoSpiderStrategy(self)

  def set_entry(self, entry):
    self._entry = entry

  def set_range(self, range):
    self._range = range

  def set_fields(self, fields):
    self._fields = fields

  def set_encoding(self, encoding):
    self._encoding = encoding

  def set_list_url_partten(self, partten):
    self.partten_list_url = partten
    self._allowed_partten['LIST'] = partten

  def set_content_url_partten(self, partten):
    self.partten_content_url = partten
    self._allowed_partten['CONTENT'] = partten

  def run(self):
    # 解析里面所有被允许的a标签
    print ('Spider Start')
    url_mgr = self.url_manager.set_domain(self._domain, self._allowed_partten)
    url_mgr.add(self._entry)
    counter = 1
    print ('Spider Running... ')
    while url_mgr.has_next():
      url = url_mgr.next()
      print url
      parser = self.strategy.get_parser(url, encoding = self._encoding)
      type = 'LIST'
      if url_mgr.is_content(url):
        type = 'CONTENT'
      try:
        new_urls, new_datas = parser.parse(url, type)
        self.dataset.add_all(new_datas)
        url_mgr.add_all(new_urls, url)
        #  counter content data
        if type == 'CONTENT':
          counter = counter + 1
          if counter > self._max: 
            break
      except Exception as e:
        print(str(e))
        continue
    
    self.dataset.store()

    print 'Spider End And Open The data.json File'
    
    