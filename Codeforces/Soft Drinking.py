# Codeforces Problem 151A - Soft Drinking

n, k, l, c, d, p, nl, np = map(int, input().split())

total_toast = min((k * l) // nl, c * d, p // np)

print(total_toast // n)
