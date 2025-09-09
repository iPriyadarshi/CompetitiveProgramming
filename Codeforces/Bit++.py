# Codeforces Problem 282A - Bit++
no_of_statements = int(input())
statements = [input().strip() for _ in range(no_of_statements)]

x = 0
for statement in statements:
    if "++" in statement:
        x += 1
    elif "--" in statement:
        x -= 1
print(x)
