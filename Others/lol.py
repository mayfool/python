import requests
headers={'DAIWAN-API-TOKEN':'12CC5-B56DD-C431B-11514'}
response=requests.get('http://lolapi.games-cube.com/UserArea?keyword=安静的疯子l',headers=headers)
print(response.text)
