# -*- coding: utf-8 -*-
# IP地址归属地的自动查询  //调用他人的接口

import requests
url = "http://m.ip138.com/ip.asp?ip="
try:
    r = requests.get(url+'202.204.80.112')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print (r.text[-500:])
except:
    print "error"
    
#python中None与NULL不同
# None的类型为NoneType
# >>>type(None)
# <class 'NoneType'>
# 用判断语句时，考虑None
# 用xx is None 语句