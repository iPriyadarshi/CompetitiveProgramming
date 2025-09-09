# Codeforces Problem 236A - Boy or Girl
username = input().strip()
unique_characters = set(username)
if len(unique_characters) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
