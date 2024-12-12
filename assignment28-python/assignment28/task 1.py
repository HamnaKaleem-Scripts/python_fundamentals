#task 1 values i nreverse order

import random
a=[0]*10
print('list = ',end='')
for i in range (10):
    a[i]=random.randint(1,10)
    print(a[i],end=' ')
print('\nreverse list=',end=' ')    
for i in range (9,-1,-1):
    print(a[i],end=' ')
