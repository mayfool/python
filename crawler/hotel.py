import urllib
import urllib.request
import json

from  bs4 import BeautifulSoup as bs
import re

'''
crawl page from hotel.elong.com
'''
#this part can be replaced by requests
place="guangzhou/"
url="http://hotel.elong.com/"+place

#headers camouflage
useragent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
headers={

    'User-Agent':useragent
}


res=urllib.request.urlopen(url)
data=res.read()
res.close()

'''
parse and select what i need
'''
#BeautifulSoup(data) will transform [data] in unicode automatically
soup=bs(data)
hotellinks=[]#define a list for hotellink
hotelnumbers=[]#define a list for hotelbumber


for tagdiv in soup.find_all('div',class_='h_info_base'):
    for tagp in tagdiv.find_all('p',class_='h_info_b1'):
        for taga in tagp.find_all('a'):
            hotellink=taga.get('href')

            #throw every hotellink to hotellinks list
            hotellinks.append(hotellink)

for hotellink_to_hotelnumber in hotellinks:
    for hotelnumber in re.findall(r'/\d*/',hotellink_to_hotelnumber):
        for hotelnumber_again in re.findall(r'\d*',hotelnumber):
            hotelnumbers.append(hotelnumber_again)


print(hotellinks,"\n")
print(hotelnumbers,"\n")