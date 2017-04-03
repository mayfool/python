import requests

roomset = set()
header = {"Cookie": "cId=77330690094598;"}
page = 1

while True:

    print(page, end="...", flush=True)

    payload = {'page': page, 'item': -3, 'live': "false"}
    page += 1

    r = requests.post("https://web.immomo.com/webmomo/api/scene/recommend/lists", data=payload, headers=header)
    js = r.json()

    [roomset.add(room['stid']) for room in js['data']['r_infos']]

    if not js['data']['h_next']:
        break

print()
for room in roomset:
    print(room)