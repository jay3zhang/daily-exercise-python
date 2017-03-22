# -*- coding: utf-8 -*-
#亚马逊商品页面爬取
#头文件伪装，模仿浏览器，否则亚马逊服务器禁止访问
import requests
url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,headers=kv)
    r.raise_for_status()
    print r.status_code
    print r.encoding
    r.encoding = r.apparent_encoding
    print r.text[3000:5000]
except:
    print "error"