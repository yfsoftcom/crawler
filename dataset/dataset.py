# dataset
import json
class Dataset(object):
    def __init__(self):
        self.datas = {}

    def get_datas(self, class_name):
        if class_name not in self.datas.keys():
            self.datas[class_name] = dict()
        return self.datas[class_name]

    def add(self, data):
        if data is None:
            return
        class_name = data.get_class_name()
        id = data.get('id')
        datas = self.get_datas(class_name)
        if id in datas.keys():
            datas[id].update(data)
        else:
            datas[id] = data
        
        self.datas[class_name] = datas

    def add_all(self, datas):
        if datas is None:
            return
        for data in datas:
            self.add(data)
    
    def store(self):
        print self.datas
        print 'store'

    def output(self):
        # print self.datas.keys()
        for datas in self.datas.values():
            for data in datas.values():
                print data


    # def add(self, data):
    #     if data is None:
    #         return
    #     if data.get('id') is None:
    #         return
    #     if data.get('id') in self.datas.keys():
    #         self.datas[data.get('id')].update(data)
    #     else:
    #         self.datas[data.get('id')] = data

    # def get_json(self):
    #     json_str = dict()
    #     for data in self.datas.values():
    #         d = data.get_dict()
    #         d['refid'] = d['id']
    #         d['src'] = 'zhilian'
    #         d['company'] = d['name']
    #         del d['id']
    #         json_str[d['refid']] = d
            
    #     return json.dumps(json_str, ensure_ascii = False)
        
    # def get_list(self):
    #     json_str = list()
    #     for data in self.datas.values():
    #         d = data.get_dict()
    #         d['refid'] = d['id']
    #         d['src'] = 'zhilian'
    #         d['company'] = d['name']
    #         del d['id']
    #         json_str.append(d)
    #     return json_str

    # def store(self):
    #     f = open('data.json', 'w')
    #     f.write(self.get_json())
    #     f.close()
        