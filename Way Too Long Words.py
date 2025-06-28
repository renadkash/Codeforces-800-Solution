"""
71A - Way Too Long Words
Difficulty:800
link:https://codeforces.com/problemset/problem/71/A
"""
#Print n lines. The i-th line should contain the result of replacing
# f the i-th word from the input data

n =int(input())

for _ in range(n):
    x = input()
    if len(x) > 10:
        print(x[0] + str(len(x)-2) + x[len(x)-1])
    else:
        print(x)