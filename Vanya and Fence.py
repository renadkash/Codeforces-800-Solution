n,h=map(int,input().split())
c=0
x=list(map(int,input().split()))
for i in range(n):
    if x[i] <= h:
        c+=1
    else:
        c+=2
print(c)