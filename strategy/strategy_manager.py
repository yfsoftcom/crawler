# -*- coding: utf-8 -*-
from zhaopin.zhaopin_strategy import ZhaoPinStrategy
from sdkcn.sdkcn_strategy import SdkcnStrategy
from car.car_strategy import CarStrategy
from ssq_wilead_com.domain_strategy import ComWileadSsqStrategy
class StrategyManager(object):
  def __init__(self):
    self.domains = dict()
    self.domains['zhaopin.com'] = ZhaoPinStrategy()
    self.domains['sdk.cn'] = SdkcnStrategy()
    self.domains['www.autohome.com.cn'] = CarStrategy()
    self.domains['ssq.wilead.com'] = ComWileadSsqStrategy()
    self.autospider_strategy = None
    
  def add_strategy(self, domain, strategy):
    self.domains[domain] = strategy

  def get_strategy(self, domain):
    return self.domains[domain]

  def has_strategy(self, domain):
    return domain in self.domains.keys()

  def get_auto_strategy(self, spider = None):
    if self.autospider_strategy is None:
      self.autospider_strategy = AutoSpiderStrategy(spider)

    return self.autospider_strategy
    



  
