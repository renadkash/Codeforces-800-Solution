"""
263A-Beutiful Matrix
Difficulty:800
link:
"""
#Print a single integer — the minimum number of moves needed to make the matrix beautiful.

matrix = []

for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            c = abs(2 - i) + abs(2 - j)

print(c)