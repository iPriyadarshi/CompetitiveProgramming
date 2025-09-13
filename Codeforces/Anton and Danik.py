# Codeforces Problem 734A - Anton and Danik

games_played = int(input())
s = input()
count = 0

for ch in s:
    if ch == "A":
        count += 1
    if ch == "D":
        count -= 1

if count > 0:
    print("Anton")
elif count < 0:
    print("Danik")
else:
    print("Friendship")
