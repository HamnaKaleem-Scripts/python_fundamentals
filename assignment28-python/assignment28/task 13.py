#task 13 print in triple form

import random
a=[0]*10
for i in range(10):
    a[i]=random.randint(3,7)
print(a)
for i in range(8):
    for j in range(i,i+3):
        print(a[j],end=' ')
    print()
