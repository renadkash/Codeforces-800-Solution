n=int(input())
c=0
while n>0:
    if n >= 100:
        n=n-100
    elif n>=20:
        n=n-20
    elif n>=10:
        n=n-10
    elif n>=5:
        n=n-5
    elif n>=1:
        n=n-1
    c+=1
print(c)