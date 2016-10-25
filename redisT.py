__author__ = 'Oliu'
# 2016/10/25
import redis

# method one
# r = redis.Redis(host='localhost', port=6379, db=0)

# method two
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

print("set key-value result: " + str(r.set('hello', 'Oliu')))
print("get key-value result: " + str(r.get('hello')))

