n1=list(input())
n2=list(input())
m=""
for i in range(len(n1)):
    if n1[i]==n2[i]:
        m+="0"
    else:
        m+="1"
print(m)