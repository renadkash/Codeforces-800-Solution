n = int(input())

p = list(map(int, input().split()))
q = list(map(int, input().split()))

x = p[1:]
y = q[1:]

s = set(x + y)
if len(s) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
