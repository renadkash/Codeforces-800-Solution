"""
282A - Bit++
Difficulty:800
link:https://codeforces.com/problemset/problem/282/A
"""
#Print a single integer — the final value of x.
i=int(input())

X = 0
for _ in range(i):
    s=input()
    if "++" in s :
        X=X+1
    if "--" in s:
        X=X-1