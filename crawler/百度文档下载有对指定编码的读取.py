#coding:utf-8
import requests
import bs4
baseUrl="https://wenku.baidu.com/view/68cd0c3031126edb6f1a10c2.html"
response=requests.get(baseUrl,"html")
print("nihao")

print("\x85")

response=response.text.encode(response.encoding).decode("gb2312")
#print(response)
#soup=bs4.BeautifulSoup(response)
#print(soup)