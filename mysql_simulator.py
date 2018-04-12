import pymysql
charset='utf-8'

connect = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='classs', port=3306)#连接mysql服务器

cur=connect.cursor()#创建数据库指针
while True:
    order=input("mySQL>")
    cur.execute("%s"%order)
    logs=cur.fetchall()
    for log in logs:
        print(log)

conct.close()
