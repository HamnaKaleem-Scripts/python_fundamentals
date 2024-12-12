#bear and three balls
n = int(input())
a = list(map(int, input().split()))
t =[] 
for i in range(n):
    for j in range(i+1, n):
        if abs(a[j]-a[i]) <= 2:
            t.append(a[i])
            t.append(a[j])

if len(t) >= 3:
    value = sorted(list(set(t)))
    for i in range(len(value)-2):
        if value[i+2] - value[i] <= 2:
            print("YES")
            exit()

print("NO") 
