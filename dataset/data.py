"""This Script For A Data Type"""
#!/usr/bin/env python
# import string
import json
class Data(object):
    """This Class For A Data Type"""
    def __init__(self):
        self._data = {}
    def get(self, key):
        """This Func For Get Value"""
        return self._data[key]
    def set(self, key, val):
        """TODO"""
        self._data[key] = val
    def __str__(self):
        """TODO"""
        return json.dumps(self._data, ensure_ascii = False)
    def __eq__(self, another):
        """TODO"""
        return self.get('id') == another.get('id')