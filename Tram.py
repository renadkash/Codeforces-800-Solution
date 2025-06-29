n=int(input())
i=1
a, b = map(int, input().split())
c = b
capacity=c
for i in range(n-1):
    if c >capacity :
        capacity = c
    a,b=map(int, input().split())
    c =c - a + b

print(capacity)