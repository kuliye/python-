import redis
class RedisHelper:
"""连接数据库并定义读写操作函数"""
    def __init__(self,host='localhost',port=6379):
        self.redis=redis.StrictRedis(host,port)
    def hget(self,hash,key):
        return self.redis.hget(hash,key)
    def hset(self,hash,key,value):
        self.redis.hset(hash,key,value)

redish=RedisHelper()

print('输入你想要添加的信息')
name=input('名字：')
price=input('价格：')
sorted=input('库存：')
redish.hset(name,'name',name)
redish.hset(name,'price',price)
redish.hset(name,'sorted',sorted)

#利用python控制台向redis数据库中以哈希方式存储商品信息数据
