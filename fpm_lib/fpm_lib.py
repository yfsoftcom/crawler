import requests
import json
url = 'http://api.yunplus.io/api'
headers = {'Content-Type': 'application/json'}

class FpmLib(object):
    def __init__(self):
        pass
    def call_func(self, method, params):
        
        params_json_str = json.dumps({
                'appkey': '123123', 
                'method': method,
                'v': '0.0.1', 
                'timestamp':'1231', 
                'sign': '123123', 
                'param': json.dumps(params, ensure_ascii = False)
            }, ensure_ascii = False)
        
        print params_json_str
        r = requests.post(url, data = params_json_str, headers = headers)
        return r.text

# if __name__ == '__main__':
#     fpm = FpmLib()
#     print fpm.call_func('common.get',{ 'table': 'api_app', 'id': 1}).text