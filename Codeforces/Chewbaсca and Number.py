# Codeforces Problem 514A - Chewbacca and Number
num = int(input())

x = 0
power = 0
while num >= 10:
    t = num % 10
    num //= 10
    if t > 4:
        t = 9 - t
    x += t * (10**power)
    power += 1
if num > 4 and num != 9:
    num = 9 - num
x += num * (10**power)
print(x)
