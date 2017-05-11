#-*- coding: utf-8 -*-
import pymysql
connect=pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    db='javademo',
    passwd='hd951113',
    charset='utf8'

)
cursor=connect.cursor()
sql="SELECT id FROM douyu.danmu where level=11"
cursor.execute(sql)

content=cursor.fetchall()

for row in content:
    info=row[0]
    info=info.encode('UTF-8')
    print(info)