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

    def output(self):
        for data in self.datas.values():
            print str(data)