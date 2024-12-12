s=input()
a=''
count=0
for i in (s):
    if i not in a:
        a+=i
        count+=1
if count%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
