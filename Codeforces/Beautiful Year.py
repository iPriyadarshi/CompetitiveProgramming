# Codeforces Problem 271A - Beautiful Year

year = int(input())
while True:
    year += 1
    if len(set(str(year))) == 4:
        print(year)
        break