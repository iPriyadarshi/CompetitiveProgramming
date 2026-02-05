for i in range(5):
    row = list(map(int, input().split()))
    if 1 in row:
        x = i + 1  # row index (1-based)
        y = row.index(1) + 1  # column index (1-based)

# Calculate Manhattan distance to center (3, 3)
moves = abs(x - 3) + abs(y - 3)
print(moves)