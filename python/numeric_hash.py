


import hashlib
value = 'something to hash'
t_value = value.encode('utf8')
h = hashlib.sha1(t_value)
#print(h.hexdigest())
n =  int(h.hexdigest(), base=16)
print(n)