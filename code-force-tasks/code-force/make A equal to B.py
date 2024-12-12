t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    count_1=0
    sol=0
    for i in a:
        if i == 1:
            count_1 += 1
    for i in b:
        if i == 1:
            count_1 -= 1
    if count_1<0:
         for i in range(n):
             if a[i]==0 and b[i]==1:
                 a[i]=1
    elif count_1>0:
         for i in range(n):
             if a[i]==1 and b[i]==0:
                 a[i]=0
    sol=abs(count_1)
    for i in range (n):
          if a[i]!=b[i]:
              sol+=1
              break
    print(sol)
