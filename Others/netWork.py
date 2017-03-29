import urllib.request
import urllib.error
import urllib


from test.test_urllib import urlopen
from idlelib.rpc import response_queue

therequest=urllib.request.Request("http://www.google.com")
try:
   response=urllib.request.urlopen(therequest)
except urllib.error.URLError as e:
   print(e)
except urllib.error.HTTPError as m:
   print(m.code)
#print(response.read())

values={"life":"life"}
data=urllib.parse.urlencode(values)
print(data)