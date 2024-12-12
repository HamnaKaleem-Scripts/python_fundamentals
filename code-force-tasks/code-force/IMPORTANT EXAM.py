#IMPORTANT EXAM
n, m = map(int, input().split())
arr = [input() for i in range(n)]
p = list(map(int, input().split()))
total=0
max_cont=0
for i in range (m):
    a=b=c=d=e=0
    for j in range(n):
        if arr[j][i]=='A':
            a+=1
        elif arr[j][i]=='B':
            b+=1
        elif arr[j][i]=='C':
            c+=1
        elif arr[j][i]=='D':
            d+=1
        elif arr[j][i]=='E':
            e+=1
    """if a>b and a>c and a>d and a>e:
        max_cont=a
    elif b>a and b>c and b>d and b>e:
        max_cont=b    
    elif c>b and c>a and c>d and c>e:
        max_cont=c
    elif d>b and d>c and d>a and d>e:
        max_cont=d
    else:
        max_cont=e"""
    max_cont=max(a,b,c,d,e)
    total+= max_cont*p[i]
print(total)
