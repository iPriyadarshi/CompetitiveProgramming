# Codeforces Problem 1030A - In Search of an Easy Problem

n = int(input())
integers = list(map(int, input().split()))

if 1 in integers:
    print("HARD")
else:
    print("EASY")
