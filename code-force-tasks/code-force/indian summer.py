#indian summer
n=int(input())
t=[]
count=0
for i in range(n):
    spe,col=input().split()
    a=spe+' '+col
    if a not in t:
        t.append(a)
        count+=1
print(count)
