#coding:utf-8
import urllib
import urllib.request
import json
import requests
import bs4

record = open("theysay2.txt", 'w', encoding='utf-8')
PageUrl=[]
BasePageUrl="http://tieba.baidu.com/f?kw=%E6%88%92%E9%99%88%E4%B8%80%E5%8F%91%E5%84%BF&ie=utf-8&pn="
for i in range(9):
    OnePageUrl="http://tieba.baidu.com/f?kw=%E6%88%92%E9%99%88%E4%B8%80%E5%8F%91%E5%84%BF&ie=utf-8&pn={}".format()
    PageUrl.append(BasePageUrl+str(i*50))
for url in PageUrl:
    response = requests.get(url )
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    #print(soup)

    pageIds=[]
    b=[]

    for tagdiv in soup.find_all('div',class_="threadlist_title pull_left j_th_tit "):
            for tagdiv in tagdiv.find_all('a'):
                pageId=tagdiv.get('href')
                #print(pageId)
                pageIds.append(pageId)
    print(len(pageIds))
    print(pageIds[0])


    BaseUrl="https://tieba.baidu.com"
    for i in  range(len(pageIds)):
        Url = BaseUrl + pageIds[i]
        response = requests.get(Url)

        soup = bs4.BeautifulSoup(response.text, "html.parser")
        # print(soup)
        contents = soup.find_all('div', "d_post_content j_d_post_content ")
        for content in contents:
            content = content.get_text()
            record.write(content)
            print(content)

record.close()



