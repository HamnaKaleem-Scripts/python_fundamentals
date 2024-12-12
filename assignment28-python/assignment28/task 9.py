#task 9

import random
a=[0]*20
for i in range(20):
    a[i]=random.randint(0,9)
print(a)    
for i in range(2,18):
    left=a[i-1]+a[i-2]
    right=a[i+1]+a[i+2]
    avg=(left+right)//4
    a[i]=avg
print(a) 
#check
  """ 
a=[3,2,0,1,2,4,6,2,1,9,8,2,3,4,6,2,0,1,3,4]
print(a)   
for i in range(2,18):
    left=a[i-1]+a[i-2]
    right=a[i+1]+a[i+2]
    avg=(left+right)//4
    a[i]=avg
print(a) 
""""
