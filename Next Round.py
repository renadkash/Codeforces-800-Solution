"""
158A - Next Round
Difficulty:800
link:https://codeforces.com/problemset/problem/158/A
"""
#Output the number of participants who advance to the next round.

n,k=map(int,input().split())
nums = list(map(int,input().split()))

c = 0
i = 0
for _ in range(n):
    if nums[i] >= nums[k-1] and nums[i] > 0 :
        c += 1
        i += 1
    else:
        i += 1
print(c)