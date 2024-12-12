#JUMBO EXTRA CHEESE 2

t=int(input())
for i in range(t):
    n= int(input())
    maxo=0
    sum_w=0
    for j in range (n):
        a,b= map(int,input().split())
        if a<b:
            sum_w+=a
            if maxo<b:
                maxo=b
        else:
            sum_w+=b
            if maxo<a:
                maxo=a
    p = 2*(sum_w + maxo)
    print(p)
