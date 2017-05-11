'''
Created on 2017年1月19日

@author: Forcast1
'''
import requests
import urllib
import bs4
import os


response = requests.get("http://tieba.baidu.com/p/4072681229")

soup = bs4.BeautifulSoup(response.text,"html.parser")
hc=soup.find_all('img',class_="BDE_Image")
img_count=1
for m in hc:
  
  img_name="%s.jpg"%img_count
  print(m)
  urllib.request.urlretrieve(m['src'],img_name)
  img_count+=1
  print(img_count)
 