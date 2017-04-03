import requests
response=requests.get("https://api.weibo.com/2/comments/show.json?access_token=2.00hiP2tBRFTGSE9c8e08b9b6GbBCxC&id=4060330377818193")
response1=requests.get("https://api.weibo.com/2/statuses/user_timeline/ids.json?access_token=2.00hiP2tBRFTGSE9c8e08b9b6GbBCxC&uid=1054009064")
print(response1.text)