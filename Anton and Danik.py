n=int(input())
s=input()
a=0
d=0
for i in range(n):
    if s[i]=='A':
        a=a+1
    else:
        d=d+1
if a < d:
    print("Danik")
if d < a:
    print("Anton")
if a == d:
    print("Friendship")