# Codeforces Problem 41A - Translation

s = input()
t = input()

n = len(s)
if s == t[::-1]:
    print("YES")
else:
    print("NO")
