#codecraft 3
s=input()
k=int(input())
a=["January","February","March","April","May","June","July","August","September","October","November","December"]
for i in range(len(a)):
    if a[i]==s:
        num=i
num+=k
i=0
count=0
while i <=(len(a)):
    if num==count:
        print(a[i])
        break
    count+=1
    i+=1
    if i==12:
        i=0
