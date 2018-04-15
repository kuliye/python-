import pymysql
import redis
class mysqlHelper():
    def __init__(self):
        self.connection=pymysql.connect(host='127.0.0.1', user='root', passwd='xieliang', db='shoping', port=3306)
        self.cur=self.connection.cursor()
    def insert(self,name,price,sorted):
        self.cur.execute("insert into good(name,price,sorted) values('%s',%s,%s)"%(name,price,sorted))
        self.connection.commit()
    def get_menber(self):
        self.cur.execute("select * from good")
        return self.cur.fetchall()
class RedisHelper:
    def __init__(self,host='localhost',port=6379):
        self.redis=redis.StrictRedis(host,port)
    def hget(self,hash,key):
        return self.redis.hget(hash,key)
    def hset(self,hash,key,value):
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
