import urllib.request
import http.cookiejar as hc

cookie = hc.CookieJar()

handler=urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(handler)

response = opener.open('http://www.baidu.com')
for item in cookie:
    print('name='+item.name)
    print('Value = '+item.value)