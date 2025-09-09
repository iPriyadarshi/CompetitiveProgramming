# Codeforces Problem 158A - Next Round
n, k = map(int, input().split())
scores = list(map(int, input().split()))

# Find the score of the k-th participant(indexed from 1)
threshold = scores[k - 1]

# Count how many participants have a score >= threshold and > 0
qualified = sum(1 for score in scores if score >= threshold and score > 0)

print(qualified)
