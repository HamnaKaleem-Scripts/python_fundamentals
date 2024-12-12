
"""
def gcd(x,y):
    if y==0:
        return x
    else:
         GCD=1
         i=1
         while(i<=x or i<=y):
             if (x%i==0 and y%i==0):
                 GCD=i
             i+=1
         return GCD"""
a,b,n=map(int,input().split())
def gcd(x,y):
    GCD=1
    i=1
    while(i<=x or i<=y):
        if (x%i==0 and y%i==0):
             GCD=i
        i+=1
    return GCD

turn=0   
while n>0:
    if turn==0:
        simon=gcd(a,n)
        n -= simon
        turn=1
    else:
        anti=gcd(b,n)
        n-=anti
        turn=0
if turn==1:
    print('0')
else:
    print('1')


       
