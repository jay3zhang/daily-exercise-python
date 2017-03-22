# -*- coding: utf-8 -*-
#京东商品页面爬取
#try-except架构
import requests
url = "https://item.jd.com/2967929.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    print r.status_code
    print r.encoding,'\t',r.apparent_encoding
    r.encoding = r.apparent_encoding
    print r.text[:1000]
except:
    print "error"