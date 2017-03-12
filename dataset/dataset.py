# dataset
import json
class Dataset(object):
    def __init__(self):
        self.datas = {}

    def add(self, data):
        if data.get('id') is None:
            return
        if data.get('id') in self.datas:
            for k in data.keys():
                self.datas[data.get('id')].set(k, data.get(k))
        else:
            self.datas[data.get('id')] = data

    def insert(self, datas):
        if type(datas) != type([]):
            self.add(datas)
        else:
            for data in datas:
                self.add(data)

    def get_json(self):
        json_str = dict()
        for data in self.datas.values():
            json_str[data.get('id')] = data.get_dict()
        return json.dumps(json_str, ensure_ascii = False)
        
    def store(self):
        f = open('data.json', 'w')
        f.write(self.get_json())
        f.close()
        