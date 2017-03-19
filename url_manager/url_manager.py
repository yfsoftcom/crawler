from single_url_manager import SingleUrlManager

class UrlManager(object):
  def __init__(self):
    self.domains = {}
    self.current_domain = 'Default'

  def set_domain(self, domain):
    self.current_domain = domain
    if domain in self.domains.keys():
      return
    self.domains[domain] = SingleUrlManager()
 
  def get_manager(self, domain = 'Default'):
    d = self.current_domain
    if domain != 'Default':
      d = domain
    self.set_domain(d)
    return self.domains[d]