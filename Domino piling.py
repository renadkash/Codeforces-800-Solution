"""
50A	Domino piling
Difficulty:800
link:https://codeforces.com/contest/50/problem/A
"""
#Output one number — the maximal number of dominoes, which can be placed

n,k=map(int,input().split())
m = n*k
print(m//2)