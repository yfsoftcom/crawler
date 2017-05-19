# dataset
import json
# from fpm_lib.fpm_lib import FpmLib
from data import Data, DataEncoder
class Dataset(object):
    def __init__(self):
        self.datas = {}
        # self.fpm = FpmLib()

    def get_datas(self, class_name):
        if class_name not in self.datas.keys():
            self.datas[class_name] = dict()
        return self.datas[class_name]

    def add(self, data):
        if data is None:
            return
        class_name = data.get_class_name()
        datas = self.get_datas(class_name)
        
        if data.has_ref_id():
            id = data.get('refid')
            datas[id].update(data)
        else:
            id = data.get('id')
            datas[id] = data
        
        self.datas[class_name] = datas

    def add_all(self, datas):
        if datas is None:
            return
        for data in datas:
            self.add(data)

    def output(self):
        # print self.datas.keys()
        for datas in self.datas.values():
            for data in datas.values():
                print data

    # def sync_fpm(self):
    #     for key, rows in self.get_list().items():
    #         try:
    #             data = self.fpm.call_func('common.create',{ 'table': key, 'row': rows }) 
    #             print json.dumps(data, ensure_ascii = False)
    #         except Exception as e:
    #             print json.dumps(e.message)

    # def add(self, data):
    #     if data is None:
    #         return
    #     if data.get('id') is None:
    #         return
    #     if data.get('id') in self.datas.keys():
    #         self.datas[data.get('id')].update(data)
    #     else:
    #         self.datas[data.get('id')] = data

    def get_json(self):
        return json.dumps(self.datas, ensure_ascii = False, cls = DataEncoder)
        
    def get_list(self):
        json_str = dict()
        for key, datas in self.datas.items():
            arr = list()
            for data in datas.values():
                d = data.get_dict()
                arr.append(d)
            json_str[key] = arr
        return json_str

    def store(self):
        f = open('data.json', 'w')
        f.write(self.get_json())
        f.close()
        

if __name__ == '__main__':
    dataset = Dataset()
    data = Data('test', {'id': 1, 'a': '123'})
    dataset.add(data)
    dataset.output()
    print dataset.get_json()