from collections import Counter

s1=input()
s2=input()
s3=input()

s4=s1 + s2
if Counter(s4) == Counter(s3) :
    print("YES")
else:
    print("NO")
