"""This Script For A Data Type"""
#!/usr/bin/env python
# import string
import json
class Data(object):
    def __init__(self):
        self._data = {}
    def get(self, key):
        return self._data[key]
    def set(self, key, val):
        self._data[key] = val
    def keys(self):
        return self._data.keys()
    def to_json(self):
        return self.__str__()
    def __str__(self):
        print self._data
        return json.dumps(self._data, ensure_ascii = True)
    def __eq__(self, another):
        return self.get('id') == another.get('id')