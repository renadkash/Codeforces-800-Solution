k,n,w=map(int,input().split())
a,b=0,0
for i in range(w):
    a=a+k*w
    w=w-1
if a <= n:
    b=0
else:
    b=a-n
print(b)
