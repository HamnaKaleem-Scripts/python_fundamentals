#HULK

n=int(input())
for i in range (1,n+1):
    if i %2!=0:
        print('I hate',end=' ')
    else:
        print('I love',end=' ')
    if i<n:
        print('that',end=' ')
    if i==n:
        print('it'
