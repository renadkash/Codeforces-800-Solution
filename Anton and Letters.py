s=input()
s=s[1:-1].strip()
if not s:
    print(0)
else:
    l=set(s.split(", "))
    print(len(l))