
class SingleUrlManager(object):
  
  def __init__(self):
    self.new_urls = []
    self.old_urls = []

  def add(self, url):
    if url is None:
      return
    if url in self.old_urls:
      return 
    if url in self.new_urls:
      return 
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