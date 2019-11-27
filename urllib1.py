
# -*- coding:utf-8 -*-
#获取并打印google首页的html
import urllib.request
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse
import  time
# print(bs)
# print(html)
def getdata(r='http://www.nufe.edu.cn/'):
    response = urllib.request.urlopen(r)
    html = response.read()
    bs = BeautifulSoup(html, "html.parser")
def getinfo(bs):
    la = bs.find_all('a')
    res=[]
    for a in la:
        if len(a.text)>0 and a.get('href') and len(a.get('href'))>2:
            res.append(a.get('href'))
    return res
def save(url,res):
    dest_str=urlparse(url)
    with open('a.json','w') as f:
        json.dump(res,f)
def main():
    response = urllib.request.urlopen('http://www.nufe.edu.cn/')
    html = response.read()
    bs = BeautifulSoup(html, "html.parser")
    res=getinfo(bs)
    for r in res:
        if r.startswith('http'):

            print(r)
if __name__ == '__main__':
    main()