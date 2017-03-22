# -*- coding: utf-8 -*-
#百度/360 搜索关键词提交
# 百度的关键词接口：
# http://www.baidu.com/s?wd=keyword
# 360的关键词接口：
# http://www.so.com/s?q=keyword

import requests
keyword = "python"
url = "http://www.baidu.com/s"
url2 = "http://www.so.com/s"
# try:
    # kv = {'wd':keyword}
    # r = requests.get(url,params=kv)
    # print (r.request.url)
    # r.raise_for_status()
    # print (len(r.text))
# except:
    # print "error"
    
try:
    kv = {'q':keyword}
    r2 = requests.get(url2,params=kv)
    print (r2.request.url)
    r2.raise_for_status()
    print (len(r2.text))
except:
    print "error"
    