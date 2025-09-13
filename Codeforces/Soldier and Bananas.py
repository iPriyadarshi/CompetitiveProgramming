# Codeforces Problem 546A - Soldier and Bananas
k, n, w = map(int, input().split())

cost_of_w_bananas = ((w * (w + 1)) // 2) * k
need_to_borrow = max(0, cost_of_w_bananas - n)
print(need_to_borrow)
