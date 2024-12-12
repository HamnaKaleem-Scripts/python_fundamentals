#ksusha the squirrel
n, k = map(int, input().split())
s = input()

count = 0
for i in range(n):
    if s[i] == '#':
       count += 1
    else:
       count = 0    
    if count == k:
        print("NO")
        break
if count != k:
    print("YES")
"""
n,k=map(int, input().split())
s=input()
for i in range(len(s)-2):
    if s[i:i+k]=='#'*k:
        print('NO')
        break
else:
    print('YES')
"""    
