import requests
import bs4
import re
base_url="https://developer.chrome.com/extensions/"
response=requests.get("https://developer.chrome.com/extensions/samples")
bs=bs4.BeautifulSoup(response.text)
links=bs.find_all(href=re.compile("zip"))

def get_Links():
 download_links=[]
 for link in links:
    download_link=base_url+link['href']
    #print(download_link)
    download_links.append(download_link)
 return download_links

def download_file(link):
    res = requests.get(link, stream=True)
    num = link.rfind('/')
    title=link[num + 1:len(link)]
    file=r"D:\chrome_extension\\"+title+".zip"
    playFile = open(file, 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile.close()



download_links=get_Links()
for link in download_links:
    print(link)
    download_file(link)




