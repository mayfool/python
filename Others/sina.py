import requests


response=requests.post("https://api.weibo.com/oauth2/access_token?client_id=3932047147&client_secret=81b3d1cd82099f799a4312a2a99b2fb7&grant_type=authorization_code&redirect_uri=http://www.163.com&code=1768b263bd94401f2e50b8cbc56d3003")
#2.00hiP2tBRFTGSE9c8e08b9b6GbBCxC
print(response.text)
