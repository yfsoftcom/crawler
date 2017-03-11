
class Data(object):
    def __init__(self):
        self._data = {}
    def get(self, key):
        return self._data[key]
    def set(self, key, val):
        self._data[key] = val

    def toString(self):
        for (k,v) in self._data.items():
            print "data:[%s]=" % k,v

    def __eq__(self, another):
        return self.get('id') == another.get('id')