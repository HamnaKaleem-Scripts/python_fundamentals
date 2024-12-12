#task 16 print indexes of 0s 2-D array

import random
a=[[random.randint(0,9)for j in range (10)]for i in range (10)]
for i in range (10):
    for j in range (10):
        print(a[i][j],end=' ')
    print()
for i in range(10):
    for j in range(10):
         if a[i][j]==0:
            print(i,j)
 
