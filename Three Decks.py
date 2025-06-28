"""

link:https://codeforces.com/contest/2104/problem/A
"""
#For each test case, output "YES" (without quotes) if Monocarp can make the number
# of cards in all three decks equal using the described operation.
# Otherwise, output "NO" (without quotes).
t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    total = a + b + c
    if total % 3 != 0:
        print("NO")
        continue
    target = total // 3
    if a > target or b > target:
        print("NO")
    else:
        print("YES")