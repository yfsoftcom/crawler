import re
class SingleUrlManager(object):
  
  def __init__(self, allowed_partten = None):
    self.new_urls = []
    self.old_urls = []
    self.allowed_partten = {}
    if allowed_partten != None: 
      for (k, v) in allowed_partten.items():
        self.allowed_partten[k] = re.compile(v)

  def is_allowed_url(self, url):
    for (k, v) in self.allowed_partten.items():
      if v.match(url) != None:
        return True
    return False

  def get_domain(self, current_url):
    return re.search(r'^((http://)|(https://))?([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}(/)', current_url).group()[0:-1]

  def get_full_url(self, url, current_url):
    # concat the domain from the current_url
    if current_url is None:
      return url
    if re.match(r'^/', url) != None:
      return self.get_domain(current_url) + url
    return url

  def is_content(self, url):
    partten = self.allowed_partten['CONTENT']
    if partten is None:
      return False
    if partten.match(url) is None:
      return False
    return True

  def add(self, url, current_url = None):
    if url is None:
      return
    url = self.get_full_url(url, current_url)
    if url in self.old_urls:
      return 
    if url in self.new_urls:
      return 
    if self.is_allowed_url(url):
      self.new_urls.append(url)
      
  def add_all(self, urls, current_url = None):
    if urls is None:
      return
    for url in urls:
      self.add(url, current_url)

  def has_next(self):
    return len(self.new_urls) > 0

  def next(self):
    url = self.new_urls.pop()
    self.old_urls.append(url)
    return url