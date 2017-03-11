# main function
import dataset, downloader, parser, urlmanager
class Spider(object):
    def __init__(self):
        self.url_manager = urlmanager.UrlManager()
        self.downloader = downloader.Downloader()
        self.parser = parser.SimpleParser()

        self.dataset = dataset.Dataset()
        self.counter = 0

    def run(self, root):
        print 'run root %s' % (root)
        self.url_manager.add(root)
        while self.url_manager.has_next():
            try:
                url = self.url_manager.next()
                html = self.downloader.download(url)
                new_urls, data = self.parser.parse(url, html)
                #self.url_manager.add_all(new_urls)
                self.dataset.insert(data)
                if(self.counter > 1000):
                    break
                self.counter = self.counter + 1

            except Exception as e:
                print(str(e))
        
        self.dataset.output()

if __name__ == '__main__':
    spider = Spider()
    spider.run('http://sou.zhaopin.com/jobs/searchresult.ashx?bj=160000&in=210500%3B160400%3B160000%3B160200%3B160600&jl=%E6%89%AC%E5%B7%9E&p=1&isadv=0')