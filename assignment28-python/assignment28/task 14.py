#task 14  print in tabular and pricipal diagonal 2-D array

import random
a=[[random.randint(0,9)for j in range (10)]for i in range (10)]
for i in range (10):
    for j in range (10):
        print(a[i][j],end=' ')
    print()
print('principal diagonal')
for i in range(10):
    for j in range(10):
        if i==j:
            print(a[i][j],end=' ')
        else:
             print(' ',end=' ')
    print()         
