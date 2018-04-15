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
   

if __name__ == '__main__':
    mysqlh=mysqlHelper()
    redish=RedisHelper()

    temp=mysqlh.get_menber()
    for info in temp:
        redish.hset('good',info[1],info)
    
#目的是将mysql中的数据信息转存入redis，以hash存储
