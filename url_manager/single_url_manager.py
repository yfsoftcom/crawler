import re
class SingleUrlManager(object):
  
  def __init__(self, allowed_partten = None):
    self.new_urls = []
    self.old_urls = []
    if allowed_partten != None: 
      self.allowed_partten = re.compile(allowed_partten) 

  def add(self, url):
    if url is None:
      return
    if url in self.old_urls:
      return 
    if url in self.new_urls:
      return 
    if self.allowed_partten is None:
      self.new_urls.append(url)
    else:
      if self.allowed_partten.match(url) != None:
        self.new_urls.append(url)
      
  def add_all(self, urls):
    if urls is None:
      return
    for url in urls:
      self.add(url)

  def has_next(self):
    return len(self.new_urls) > 0

  def next(self):
    url = self.new_urls.pop()
    self.old_urls.append(url)
    return url