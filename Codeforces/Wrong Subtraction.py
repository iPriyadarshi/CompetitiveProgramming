# Codeforces Problem 977A - Wrong Subtraction
n, k = map(int, input().split())

for i in range(k):
    last_digit = n % 10
    if last_digit == 0:
        n = n // 10
    else:
        n -= 1
print(n)
