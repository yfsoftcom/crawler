import re
if __name__ == '__main__':
  print re.search('http://www.autohome.com.cn/ashx/AjaxIndexCarFind.ashx?type=3&value=33', s).group() 