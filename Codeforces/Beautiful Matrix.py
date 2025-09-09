# Codeforces Problem 263A - Beautiful Matrix
matrix = [list(map(int, input().split())) for _ in range(5)]
for i in range(1, 6):
    for j in range(1, 6):
        if matrix[i][j] == 1:
            print(abs(i - 3) + abs(j - 3))
            break
