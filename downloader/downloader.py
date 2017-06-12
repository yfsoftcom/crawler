# downloader
import requests
class Downloader(object):
    def __init__(self):
        pass

    def download(self, url):
        UA = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.13 Safari/537.36"
        header = { "User-Agent" : UA }
        r = requests.get(url, headers = header)
        r.encoding = 'utf8'
        return r.text

    