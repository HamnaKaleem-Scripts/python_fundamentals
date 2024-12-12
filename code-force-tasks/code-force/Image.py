#IMAGE
t=int(input())
for i in range(t):
    value=3
    x=input().strip()
    y=input().strip()
    if x[0]==x[1]or x[0]==y[0] or x[0]==y[1]:
        value-=1
    if x[1]==y[0]or x[1]==y[1]:
        value-=1
    if y[0]==y[1]:
        value-=1
    print(value)
