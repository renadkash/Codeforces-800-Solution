a=list(map(int, input().split()))
s=input()
c=0
for i in range(len(s)):
    b=int(s[i])
    c+=a[b-1]
print(c)