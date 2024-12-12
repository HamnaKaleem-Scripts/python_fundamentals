#TWO ELEVATORS

t=int(input())
for i in range (t):
    a,b,c=map(int, input().split())
    a_return=a-1
    b_return=abs(c-1)+abs(c-b)  
    if a_return<b_return or a==1:
        print('1')
    elif a_return>b_return:
        print('2')
    elif a_return==b_return:
        print('3')
