n=int(input())
x=list(map(int,input().split()))
i=0
res=[0]*n
while i < n:
    b=int(x[i])
    res[b-1]=i+1
    i+=1
print(*res)
