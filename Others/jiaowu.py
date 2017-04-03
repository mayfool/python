import requests
def login(email, password):
    login_url = 'http://bkjws.sdu.edu.cn/b/ajaxLogin'
    data = {
        'j_username': '201400301037',
        'j_password': '951113',
        }
    response = requests.post(login_url, data=data)
    login_code = response.json()
    print(login_code)



email = "493360037@qq.com"
password = "hd951113"
login(email, password)