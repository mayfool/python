import requests
import bs4

response=requests.get("http://weibo.com/p/1005051054009064/home?from=page_100505_profile&wvr=6&mod=data&is_hot=1#1490094822678")
soup=bs4.BeautifulSoup(response.text)
one=soup.find_all(class_="WB_feed_repeat S_bg1")
print(one)