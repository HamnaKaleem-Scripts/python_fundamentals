# way to LONG WORDS
n=int(input())
for i in range (n):
    w=input()
    l=len(w)
    if l>10:
        print(f'{w[0]}{(l-2)}{w[l-1]}')
    else:
        print(w)
