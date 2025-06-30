n=int(input())
s=""
for i in range(1,n+1):
    s+="I "
    if i%2 != 0:
        s+="hate"
    else:
        s+="love"
    if i==n:
        s+=" it"
    else:
        s+=" that "
print(s)