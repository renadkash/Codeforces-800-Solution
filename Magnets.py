n=int(input())
s=input()
c=1
for i in range(n-1):
    a=input()
    if s != a:
        c+=1
        s = a
print(c)
