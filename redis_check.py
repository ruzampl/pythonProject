import redis

r = redis.StrictRedis(host='sf5sandbox-redis', port=6379, db=0)
print ("set key1 123")
print (r.set('key1', '123'))
print ("get key1")
print(r.get('key1'))


for key in r.scan_iter("*"):
    print(r.get(key))