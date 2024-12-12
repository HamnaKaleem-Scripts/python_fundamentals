#task 3 copying elements

import random
a=[0]*10
b=[0]*10

for i in range (10):
    a[i]=random.randint(1,10)
print('list 1 = ',a)
for i in range(10):
    b[i]=a[i]
print('list 2 = ',b)
