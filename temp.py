import time
from datetime import datetime, timedelta

'''t = time.localtime()
print(time.ctime())
future = time.time() + 60
print(future)

print(time.ctime(future))
current_time = time.strftime("%H:%M:%S", t)
print(current_time)
print(timedelta(minutes = 10))'''

'''now = time.time()
future_time = now + 5
while  now <= future_time:
    now = time.time() 
    print("time left")
else:
    print("time finished")'''


#now_plus_10 = now + timedelta(minutes = 1)
#print(now_plus_10)

print(time.time())