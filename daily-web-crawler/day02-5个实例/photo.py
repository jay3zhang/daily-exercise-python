# -*- coding: utf-8 -*-
#网页图片爬取和存储
import requests
import os
url = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
root = "E://python//"
path = root+url.split('/')[-1]
try:
    #存放目录是否存在，不存在则创建一个
    if not os.path.exists(root):
        os.mkdir(root)
        #查看文件是否已存在
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print "success"
    else:
        print "exist!"
except:
    print "error"