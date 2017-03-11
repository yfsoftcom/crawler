# dataset

class Dataset(object):
    def __init__(self):
        self.datas = set()

    def insert(self, datas):
        for data in datas:
            self.datas.add(data)

    def output(self):
        for data in self.datas:
            data.toString()