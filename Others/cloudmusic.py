import requests
data={"s":"好久不见",
      'type':1
}
response=requests.post("http://music.163.com/api/search/get",data=data)

print(response.text)