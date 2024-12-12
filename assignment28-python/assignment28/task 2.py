#task 2 sum of all elements

import random
a=[0]*10
sum=0
print('list = ',end='')
for i in range (10):
    a[i]=random.randint(1,10)
    print(a[i],end=' ')
    sum+=a[i]
print('\nsum= ',sum)    
