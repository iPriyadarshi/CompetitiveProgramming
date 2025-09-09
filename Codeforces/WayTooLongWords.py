# Codeforces Problem 71A - Way Too Long Words
m = int(input())
words = [input().strip() for _ in range(m)]

for word in words:
    if len(word) > 10:
        print(f"{word[0]}{len(word) - 2}{word[-1]}")
    else:
        print(word)