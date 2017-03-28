# -*- coding: utf-8 -*-
from zhaopin.zhaopin_strategy import ZhaoPinStrategy
from sdkcn.sdkcn_strategy import SdkcnStrategy
class StrategyManager(object):
  def __init__(self):
    self.domains = dict()
    self.domains['zhaopin.com'] = ZhaoPinStrategy()
    self.domains['sdk.cn'] = SdkcnStrategy()

  def add_strategy(self, domain, strategy):
    self.domains[domain] = strategy

  def get_strategy(self, domain):
    return self.domains[domain]


  
