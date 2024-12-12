t= int (input())
for i in range(t):
    n=int(input())
    s=input().split()
    q_count=0
    for j in(s):
        if j=='Q':
            q_count+=1
        else:
            q_count-=1
        if q_count<0:
            q_count=0
    if q_count==0:
        print('yes')
    else :
        print('no')
    

        
