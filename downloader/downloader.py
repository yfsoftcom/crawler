# downloader
import urllib2
class Downloader(object):
    def __init__(self):
        pass

    def download(self, url):
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read()

    