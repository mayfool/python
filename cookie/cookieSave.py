import urllib.request as ur
import http.cookiejar as hc


filename = 'd:/cookie.txt'

cookie = hc.MozillaCookieJar(filename)

handler = ur.HTTPCookieProcessor(cookie)

opener = ur.build_opener(handler)

response = opener.open("http://www.baidu.com")

cookie.save(ignore_discard=True, ignore_expires=True)