s=input()

b=[int(i)for i in s.split('+')]
b.sort()
c="+".join(str(i) for i in b)
print(c)



