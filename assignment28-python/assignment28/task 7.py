#task 7

import random
a=[0]*10

for i in range(10):
    a[i]=random.randint(1,5)
print(a)
for i in range (10):
    
    print(f'{a[i]} is at index ',end='')
    for j in range (10):
        if a[i]==a[j]:
            print(j,end=' ')
           
    print()
"""
s=[]
    if a[i] not in s:
         print(f'{a[i]} is at index ',end='')
         s.append(a[i])
"""
