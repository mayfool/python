'''
Created on 2017年1月19日

@author: Forcast1
'''
import requests
import bs4

for n in range(1295,1500):
    response = requests.get("http://wufazhuce.com/one/"+str(n))
    soup = bs4.BeautifulSoup(response.text,"html.parser")
    st=soup.title.string
    fp=open("d:/new/fileA.txt",'wb')
    fp.write("hello")
    fp.close
    for meta in soup.select('meta'):
       if(meta.get('name')=='description'):
        print( meta.get('content'))