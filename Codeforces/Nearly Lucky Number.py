# Codeforces Problem 110A - Nearly Lucky Number

n = input()
count_4 = n.count("4")
count_7 = n.count("7")

lucky_digits = count_4 + count_7

if lucky_digits == 4 or lucky_digits == 7:
    print("YES")
else:
    print("NO")
