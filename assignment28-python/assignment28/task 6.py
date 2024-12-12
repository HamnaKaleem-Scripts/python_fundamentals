#task 6

import random
a=[0]*10
for i in range (10):
    r=random.randint(1,15)
    while r in a:
        r=random.randint(1,15)
    if r not in a:
        a[i]=r
print(a)
#method 2
import random
a=[]
while len(a)<10:
    r=random.randint(1,15)
    if r not in a:
        a.append(r)
print(a)
