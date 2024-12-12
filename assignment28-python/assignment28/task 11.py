#task 11

import random
a=[0]*10
for i in range(10):
    a[i]=random.randint(3,7)
print(a)
for i in range(11):
    for j in range(i):
        print(a[j],end=' ')
    print(
