# Codeforces Problem 266A - Stones on the Table
no_of_stones = int(input())
stones = input()
count = 0
for i in range(1, no_of_stones):
    if stones[i] == stones[i - 1]:
        count += 1
print(count)