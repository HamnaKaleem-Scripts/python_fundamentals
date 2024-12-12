#task 15 replace 0 with 1 2-D array

import random
a=[[random.randint(0,9)for j in range (10)]for i in range (10)]
for i in range (10):
    for j in range (10):
        print(a[i][j],end=' ')
    print()
for i in range (10):
    for j in range (10):
        if a[i][j]==0:
            a[i][j]=1
print()            
for i in range (10):
    for j in range (10):
        print(a[i][j],end=' ')
    print()            
