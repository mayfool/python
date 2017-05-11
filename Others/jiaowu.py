import requests
def login(email, password):
    session=requests.session()
    login_url = 'http://bkjws.sdu.edu.cn/b/ajaxLogin'
    data = {
        'j_username':email,
        'j_password': password,
        }
    response = session.post(login_url, data=data)
    login_code = response.json()
    another=session.get("http://bkjws.sdu.edu.cn/f/grxx/xs/lxfs")
    print(another.text)



email = "201400301037"
password = "951113"
login(email, password)