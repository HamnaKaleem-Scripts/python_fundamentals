#task 12

import random
a=[0]*10
for i in range(10):
    a[i]=random.randint(3,7)
print(a)
for i in range(11):
    sum=0
    for j in range(i):
        print(a[j],end=' ')
        sum+=a[j]
        if j==i-1:
            print(f'={sum}')
