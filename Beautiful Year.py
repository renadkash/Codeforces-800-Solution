n = int(input())
n += 1

while True:
    digits = [int(d) for d in str(n)]
    if len(set(digits)) == len(digits):
        print(n)
        break
    n += 1

