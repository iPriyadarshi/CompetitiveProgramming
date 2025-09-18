# Codeforces Problem 344A - Magnets

n = int(input())
for i in range(n):
    s = input().strip()
    if i == 0:
        count = 1
        prev = s
    else:
        if s != prev:
            count += 1
            prev = s
print(count)
