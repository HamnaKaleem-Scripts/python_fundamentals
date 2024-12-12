t=int(input())
for i in range (t):
    n=int(input())
    a=list(map(int,input().split()))
    value=0
    for j in range(n):
        q=a[j]
        for k in range(j+1,n):
            if q==a[k]:
                value=1
                break
        if value==1:
            break
    if value==1:
        print('NO')
    elif value==0:
        print('YES')
