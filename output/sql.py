# -*- coding: utf-8 -*-

import json
import sys
import requests
reload(sys)
sys.setdefaultencoding('utf8')

def generate_brand(items):
    sql = 'insert into fpm_car_brand(id, name, firstletter, logo) values '
    vals = []
    for id, item in items:
        val = "( %d, '%s', '%s', '%s')" % (int(id), item['name'], item['firstletter'], item['logo'])
        vals.append(val)
    sql = sql + ','.join(vals)
    f = open('brand.sql', 'w')
    f.write(sql)
    f.close()

def download_brand(items):
    for id, item in items:
        url = item['logo']
        print url
        r = requests.get(url, stream=True)
        r.raw
        f = open('%s.jpg' % str(id), 'wb')
        f.write(r.content)
        f.close()

def generate_series(items):
    sql = 'insert into fpm_car_series(id, pid, name, firstletter) values '
    vals = []
    for id, item in items:
        val = '(' + str(id) + ',' + str(item['pid']) + ", '" + item['name'] + "', '" + item['firstletter'] + "'" + ')'
        vals.append(val)
    sql = sql + ','.join(vals)
    f = open('series.sql', 'w')
    f.write(sql)
    f.close()

def generate_sub_series(items):
    sql = 'insert into fpm_car_sub_series(id, pid, name, firstletter, seriesorder, seriesstate) values '
    vals = []
    for id, item in items:
        val = ','.join([
            '(' + str(id),
            str(item['pid']),
            "'" + item['name'] + "'",
            "'" + item['firstletter'] + "'",
            str(item['seriesorder']),
            str(item['seriesstate']) + ')',
        ])
        vals.append(val)
    sql = sql + ','.join(vals)
    f = open('sub_series.sql', 'w')
    f.write(sql)
    f.close()

def generate_year(items):
    sql = 'insert into fpm_car_year(id, pid, name) values '
    vals = []
    for id, item in items:
        val = ','.join([
            '(' + str(id),
            str(item['pid']),
            "'" + item['name'] + "')",
        ])
        vals.append(val)
    sql = sql + ','.join(vals)
    f = open('year.sql', 'w')
    f.write(sql)
    f.close()

def generate_spec(items):
    sql = 'insert into fpm_car_spec(id, pid, name, maxprice, state, minprice) values '
    vals = []
    counter = 0
    f = open('spec.sql', 'w')
    for id, item in items:
        val = ','.join([
            '(' + str(id),
            str(item['pid']),
            "'" + item['name'] + "'",
            str(item['maxprice']),
            str(item['state']),
            str(item['minprice']) + ')',
        ])
        vals.append(val)
        counter = counter + 1
        if counter == 2000:
            counter = 0
            _sql = sql + ','.join(vals) + ';\n\n\n\n'
            f.write(_sql)
            vals = []
    
    if counter > 0:
        _sql = sql + ','.join(vals) + ';'
        f.write(_sql)
    f.close()

if __name__ == '__main__':
    f = file('car.json')
    obj = json.load(f)
    # brand  --------
    # generate_brand(obj['brand'].items())
    # print 'brand ok'
    # download brand logos
    download_brand(obj['brand'].items())
    print 'download_brand ok'
    # generate_series(obj['series'].items())
    # print 'series ok'
    # generate_sub_series(obj['sub_series'].items())
    # print 'sub_series ok'
    # generate_year(obj['year'].items())
    # print 'year ok'
    # print len(obj['spec'])
    # generate_spec(obj['spec'].items())
    # print 'spec ok'

