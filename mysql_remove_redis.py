import pymysql
import redis
class mysqlHelper():
    def __init__(self):
        """连接mysql数据库并定义指针"""
        self.connection=pymysql.connect(host='127.0.0.1', user='root', passwd='xieliang', db='shoping', port=3306)
        self.cur=self.connection.cursor()

    def get_menber(self):
        """"获取值"""
        self.cur.execute("select * from good")
        return self.cur.fetchall()
    
class RedisHelper:
    def __init__(self,host='localhost',port=6379):
        """连接redis数据库"""
        self.redis=redis.StrictRedis(host,port)
        
    def hset(self,hash,key,value):
        """设置值"""
        self.redis.hset(hash,key,value)
        
mysqlh=mysqlHelper()
redish=RedisHelper()


temp=mysqlh.get_menber()
for good in temp:
    name=good[1]
    price=good[2]
    sorted=good[3]
    redish.hset(name,'name',name)
    redish.hset(name,'price',price)
    redish.hset(name,'sorted',sorted)
#目的是将mysql中的代码存入redis，以hash存储
