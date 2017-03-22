﻿# -*- coding: utf-8 -*-
#python2
import requests
import bs4
from bs4 import BeautifulSoup
#解决中文编码问题
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[3].string])

def printUnivList(ulist,num):
    tplt = "{0:<10}\t{1:<20}\t\t{2:<10}"
    print(tplt.format("排名","学校名称","总分",unichr(12288).encode('utf-8')))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],unichr(12288).encode('utf-8')))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,10)

main()

