import sys


import time
import os
from os.path import exists
import json
import codecs
import gzip
import io

import urllib
import urllib.request

import re


def getComment(hotelnumber,Pgnum_max):


    for page in range(Pgnum_max):

        Comments=[]

        page=str(page)
        print ("第"+page+"页")

        url="http://hotel.elong.com/ajax/detail/gethotelreviews/?hotelId="+hotelnumber+"&recommendedType=0&pageIndex="+page+"&mainTagId=0&subTagId=0&_=1468730838292"
        headers={

            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Connection':'keep-alive',
            'X-Requested-With':'XMLHttpRequest',
            #'Referer':'http://hotel.elong.com/guangzhou/32001005/',
            'Host':'hotel.elong.com'

        }


        #请求AJAX
        req=urllib.request.Request(url,None,headers)
        res=urllib.request.urlopen(url)
        data=res.read()
        res.close()

        #因为data有压缩所以要从内存中读出来解压
        print(data)
        data=data.decode()
        ungz=data
        print(ungz)
        #正则提取
        pattern_Comment=re.compile(r'"content":"\W*"')
        #仍不能完全匹配到所有用户，这里只是匹配到中文名的用户，可能要用到非贪婪模式！
        pattern_username=re.compile(r'"nickName":"\W*"')
        pattern_CommentTime=re.compile(r'"createTimeString":"....-..-..\s..:..:.."')


        for username in re.findall(pattern_username,ungz):
            # print type(username)
            # print username,'\n'
            Comments.append(username)


        for CommentTime in re.findall(pattern_CommentTime,ungz):
            # print type(CommentTime)
            # print CommentTime,'\n'
            Comments.append(CommentTime)


        for Comment in re.findall(pattern_Comment,ungz):
            # print Comment,'\n'
            # print type(Comment)
            Comments.append(Comment)

        #保存成HTML
        comment=",".join(Comments)#list转str

        cdir = u'./Comments/'
        if not exists(cdir):
            os.makedirs(cdir)

        f=codecs.open(cdir+u'page'+page+u'.txt','wb+','utf-8')
        f.write(comment)

'''
程序入口
'''
#前面也是没有做完，所以酒店编号列表先构造一个
hotelnumber_list=['32001005']
#前面没有抓到最大评论页面数，先假定最大有200页
Pgnum_max=2
for hotelnumber in hotelnumber_list:
    getComment(hotelnumber,Pgnum_max)