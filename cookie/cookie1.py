'''
Created on 2017年1月8日

@author: Forcast1
'''
import urllib.request
import http.cookiejar as hc

cookie = hc.CookieJar()

handler=urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(handler)

