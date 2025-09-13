# Codeforces Problem 116A - Tram

n = int(input())
capacity = 0
curr_people = 0

for stop in range(1, n + 1):
    a, b = map(int, input().split())
    curr_people -= a
    curr_people += b
    capacity = max(capacity, curr_people)
print(capacity)
