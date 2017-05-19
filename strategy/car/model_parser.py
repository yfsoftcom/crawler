from lxml import etree
from dataset.data import Data
from strategy.car.car_parser import CarParser
import re
class ModelParser(CarParser):

    def _get_new_data(self, dom):
        new_datas = []
        pid = self.get_url_value()
        try:
            datas = dom['result']['yearitems']
            for d in datas:
                d_id = d['id']
                data = Data('year')
                data.set('id', d_id)
                data.set('name', d['name'])
                data.set('pid', pid)
                new_datas.append(data)
                spec = d['specitems']
                for sub_d in spec:
                    sub_data = Data('spec', sub_d)
                    sub_data.set('pid', d_id)
                    new_datas.append(sub_data)
                
        except Exception as e:
            print(str(e))
        return new_datas

#######
# year
# {"pid": 210, "id": 8192, "name": "2016款"}
# spec
# {"name": "2004款 1.3L AT", "pid": 275, "maxprice": 80800, "state": 40, "minprice": 80800, "id": 18}