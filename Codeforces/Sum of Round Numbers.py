# Codeforces Problem 1352A - Sum of Round Numbers
t = int(input())

for _ in range(t):
    n = int(input())
    round_nums = []

    place = 1
    while n > 0:
        digit = n % 10
        if digit != 0:
            round_nums.append(digit * place)
        n //= 10
        place *= 10

    print(len(round_nums))
    print(*round_nums)
