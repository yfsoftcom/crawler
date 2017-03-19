class Strategy(object):
  def __init__(self):
    pass

  def get_parser(self, url):
    return None

  def _filter(self, input):
    return input

  def validate(self, dataset):
    return filter(self._filter ,dataset)