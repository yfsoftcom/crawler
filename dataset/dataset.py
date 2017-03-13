# dataset
import json
class Dataset(object):
    def __init__(self):
        self.datas = {}

    def add(self, data):
        if data is None:
            return
        if data.get('id') is None:
            return
        if data.get('id') in self.datas.keys():
            self.datas[data.get('id')].update(data)
        else:
            self.datas[data.get('id')] = data

    def insert(self, datas):
        if datas is None:
            return
        if isinstance(datas, list):
            for data in datas:
                self.add(data)
        else:
            if datas.get('id') is None:
                return
            self.add(datas)

    def get_json(self):
        json_str = dict()
        for data in self.datas.values():
            d = data.get_dict()
            d['refid'] = d['id']
            d['src'] = 'zhilian'
            d['company'] = d['name']
            del d['id']
            json_str[d['refid']] = d
            
        return json.dumps(json_str, ensure_ascii = False)
        
    def get_list(self):
        json_str = list()
        for data in self.datas.values():
            d = data.get_dict()
            d['refid'] = d['id']
            d['src'] = 'zhilian'
            d['company'] = d['name']
            del d['id']
            json_str.append(d)
        return json_str

    def store(self):
        f = open('data.json', 'w')
        f.write(self.get_json())
        f.close()
        