#task 10

import random
a=[0]*10
for i in range(10):
    a[i]=random.randint(3,7)
print(a)    
for i in range(10):
    count=0
    while count<a[i]:
        print('*',end='')
        count+=1
    print()    
