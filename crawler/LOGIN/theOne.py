import urllib
import requests as req
loginurl='http://192.168.8.10/portal/index_default.jsp?Language=Chinese'
formData={'form_email':'493360037@qq.com',
          'form_password':'hd951113'}
formdata={'Language':	'Chinese',
'ClientIP': '211.87.237.131',
'sessionID': '-2074570028169500506',
'timeoutvalue':	'45',
'heartbeat'	:'240',
'fastwebornot'	:'false',
'username' :	'201400301037',
'password' :'131415',
'strOldPrivateIP':'211.87.237.131',
'strOldPublicIP':	'211.87.237.131',
'strPrivateIP':'211.87.237.131',
'PublicIP':	'211.87.237.131',
'iIPCONFIG':	'0',
'sHttpPrefix':	'http://192.168.8.10',

          }
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:9.0.1) Gecko/20100101 Firefox/9.0.1'}
res=req.post(loginurl,data=formdata,headers=headers,verify=False)

print(res.text)
