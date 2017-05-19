from lxml import etree
from dataset.data import Data
from strategy.car.car_parser import CarParser
import re
class SeriesParser(CarParser):

    def _get_new_data(self, dom):
        self._new_urls = []
        new_datas = []
        pid = self.get_url_value()
        try:
            datas = dom['result']['factoryitems']
            for d in datas:
                d_id = d['id']
                data = Data('series')
                data.set('id', d_id)
                data.set('name', d['name'])
                data.set('pid', pid)
                data.set('firstletter', d['firstletter'])

                new_datas.append(data)
                sub_datas = d['seriesitems']
                for sub_d in sub_datas:
                    sub_data = Data('sub_series', sub_d)
                    sub_data.set('pid', d_id)
                    new_datas.append(sub_data)
                    self._new_urls.append('http://www.autohome.com.cn/ashx/AjaxIndexCarFind.ashx?type=5&value=' + str(sub_d['id']))
        except Exception as e:
            print(str(e))
        return new_datas

    def _get_new_urls(self, page_url, dom):
        return self._new_urls

    def _get_next_page_url(self, dom):
        pass

######
# sub_series
# {"name": "赛弗", "pid": 4, "firstletter": "S", "seriesstate": 40, "id": 6, "seriesorder": 684}
# series
# {"pid": 57, "id": 3, "firstletter": "M", "name": "玛莎拉蒂"}
#
######