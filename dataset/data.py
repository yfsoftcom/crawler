"""This Script For A Data Type"""
#!/usr/bin/env python
# import string
import json
class Data(object):

    def __init__(self, className, data = {}):
        self._class_name = className
        self._data = data

    def get_class_name(self):
        return self._class_name

    def get(self, key):
        if key == 'refid':
            if 'refid' in self._data:
                return self._data[key]
            else:
                return self._data['id']
        return self._data[key]

    def set(self, key, val):
        self._data[key] = val

    def keys(self):
        return self._data.keys()

    def update(self, data):
        self._data.update(data.get_dict())

    def to_json(self):
        return self.__str__()

    def get_dict(self):
        return self._data

    def __str__(self):
        return json.dumps(self._data, ensure_ascii = False)
        
    def __eq__(self, another):
        return self.get('refid') == another.get('refid') and self.get_class_name() == another.get_class_name()


class DataEncoder(json.JSONEncoder):
    def default(self, obj):  
        if isinstance(obj, Data):  
            return obj.__str__()  
        return json.JSONEncoder.default(self, obj)  
