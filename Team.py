"""
231A - Team
Difficulty:800
link:https://codeforces.com/contest/231/problem/A
"""
#Print a single integer — the number of problems the friends will implement on the contest
n=int(input())

i = 0
for _ in range(n):
    a,b,c=map(int,input().split())
    if a+b+c>= 2:
        i=i+1
print(i)