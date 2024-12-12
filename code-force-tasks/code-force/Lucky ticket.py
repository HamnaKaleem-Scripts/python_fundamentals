
n=int(input())
s=input()
value=1
t=n//2
for i in (s):
    if (i=='4' or i=='7') and value==1:
        value=1
    else:
         value=0
if value==0:
    print('NO')
else:
    sum_first=0
    sum_second=0
    count=0
    for j in (s):
        if count<t:
            sum_first+=int(j)
        else:
            sum_second+=int(j)
        count+=1   
        
    
    if sum_first==sum_second:
        print('YES')
    else:
        print('NO'
