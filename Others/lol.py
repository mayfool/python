import requests
import json
headers={'DAIWAN-API-TOKEN':'7427E-5F617-67E4C-7CEE6'}

def getuinandvaidById():
    response = requests.get('http://lolapi.games-cube.com/UserArea?keyword=安静的疯子l', headers=headers)

    js = response.json()['data']
    a = []
    b = []
    c={}
    for i in js:
        if i['level'] == 30:
            a.append(i['area_id'])
            b.append(i['qquin'])
            c[i['area_id']]=i['qquin']
    return a,b,c

def getPower(qquin=0,vaid=0):
    payload={'qquin':qquin,'vaid':vaid}
    response=requests.get('http://lolapi.games-cube.com/UserHotInfo',params=payload,headers=headers)
    return response.json()



qa=getuinandvaidById()
qquin=qa[1][0]
vaid=qa[0][0]
print(getPower(qquin,vaid))
