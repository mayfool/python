
import requests
headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, sdch",
"Accept-Language":"zh-CN,zh;q=0.8",
"Cache-Control":"max-age=0","Cookie":"filterFlag=false; hello1=201400301037; hello2=true; hello5=; hello3=%CE%CC%CE%CB%CE%CA; JSESSIONID=837ECEFDB9250C8980E53D42EE0EB10E; JSESSIONID=95432FC5966A5AA6619BB37603D9CB60","Host":"192.168.8.10",
"Origin":"http://192.168.8.10","Proxy-Connection":"keep-alive",
"Content-Type":"application/x-www-form-urlencoded","Referer":"http://192.168.8.10/portal/index.jsp",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}
#cookies={'JSESSIONID':'FCFF19F1E3DF0880A3E12D2E43EE67E8', 'filterFlag':'true' ,'hello1':'201400301037','hello2':'false', 'hello5':'', 'hello3':' ','JSESSIONID':'78D7AD4A48AED3DF4C1B29FD15C97B1B'}
cookies={}
data={"username":"201400301037","password":"131415"}
raw_cookies="JSESSIONID=D2224E51531CE9F2F2A47907C45E2CCD; filterFlag=false; hello1=201400301037; hello2=true; hello5=; hello3=%CE%CC%CE%CB%CE%CA; JSESSIONID=86504FC4E4DEA2023856045B06BE7555"
for line in raw_cookies.split(';'):
  key,value=line.split('=',1)#1代表只分一次，得到两个数据
  cookies[key]=value

response=requests.post('http://192.168.8.10/portal/login.jsp?Flag=0',headers=headers,data=data)
print(response.text
      )