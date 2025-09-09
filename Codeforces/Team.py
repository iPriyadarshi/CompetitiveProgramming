# Codeforces Problem 231A - Team
no_of_problems = int(input())
problems = [list(map(int, input().split())) for _ in range(no_of_problems)]
successful_problems = sum(1 for problem in problems if sum(problem) >= 2)
print(successful_problems)
