n=int(input())
total=0
for i in range (n):
    count=0
    s=input()
    for j in (s):
        if j=='1':
            count+=1
    if count>=2:
        total+=1
print(total)      
    
#using split()
n=int(input())
total=0
for i in range (n):
    count=0
    v1,v2,v3=map(int,input().split())
    if v1==1:
        count+=1
    if v2==1:
        count+=1
    if v3==1:
        count+=1
    if count>=2:
        total+=1
print(total)        
        
        
    
