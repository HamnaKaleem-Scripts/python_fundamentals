#task 5

import random
a=[0]*10
count_e=0
count_o=0
for i in range (10):
    a[i]=random.randint(1,100)
print('list= ',a)
print("Even num =",end='')
for i in range (10):
    if a[i]%2==0:
        print(a[i],end=' ')
        count_e+=1
print('\nCount of even numbers = ',count_e)
print('Odd num = ',end='')
for i in range (10):
    if a[i]%2!=0:
        print(a[i],end=' ')
        count_o+=1
print('\n Count of odd numbers = ',count_o)
if count_e>count_o:
    for i in range (10):
        if a[i]%2!=0:
            a[i]+=1
elif count_o>count_e:
    for i in range (10):
        if a[i]%2==0:
            a[i]-=1
print (a)            
