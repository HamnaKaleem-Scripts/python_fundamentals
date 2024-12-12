#task 8
import random
a=[0]*20
n=10
for i in range(20):
    if i>0:
        a[i]=random.randint(a[i-1]+1,n)
    else:
        a[i]=random.randint(1,10)
    n+=2    
print(a)
#print ('random nummbers between 1 to',n)
for i in range (19):
    n=1
    r=a[i]
    while r<a[i+1]:
        if r+1!=a[i+1]:
            print(a[i]+n,end=' ')
        
        n+=1
        r+=1

