# Codeforces Problem 617A - Elephant
x = int(input())
steps = 0
for step_length in range(5, 0, -1):
    while x >= step_length:
        x -= step_length
        steps += 1
print(steps)
