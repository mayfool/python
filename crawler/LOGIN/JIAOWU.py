import urllib.request as ur
import urllib
import http.cookiejar as hc
filename = 'cookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = hc.MozillaCookieJar(filename)
opener = ur.build_opener(ur.HTTPCookieProcessor(cookie))
postdata = urllib.parse.urlencode({
            'login_strLoginName':'201400301037',
            'login_strLoginPassword':'bks131415'
        }).encode(encoding='utf-8')
# 登录教务系统的URL
loginUrl = 'http://www.bksms.sdu.edu.cn/login'
# 模拟登录，并把cookie保存到变量
result = opener.open(loginUrl,postdata)
# 保存cookie到cookie.txt中
'''
cookie.save(ignore_discard=True, ignore_expires=True)
# 利用cookie请求访问另一个网址，此网址是成绩查询网址
gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
# 请求访问成绩查询网址
result = opener.open(gradeUrl)'''
print (result.read())