# downloader
import requests
class Downloader(object):
    def __init__(self):
        pass

    def download(self, url):
        r = requests.get(url)
        return r.text

    