#task 4

def bubble_sort(x):
    for j in range(len(x)-1):
        for i in range(len(x)-1):
            if x[i]>x[i+1]:
                x[i],x[i+1]=x[i+1],x[i]
    return x
import random
a=[0]*5
b=[0]*5
c=[0]*10
for i in range (5):
    a[i]=random.randint(1,50)
    b[i]=random.randint(1,50)
l1=bubble_sort(a)
l2=bubble_sort(b)
print('list 1 = ',l1)
print('lest 2 = ',l2)
for i in range (10):
    if i<5:
        c[i]=l1[i]
    else:
        c[i]=l2[i-5]
l3=bubble_sort (c)
print('list 3 = ',l3)
