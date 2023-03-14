n, k = map(int, input().split())

score = list(map(int, input().split()))
score.sort(reverse=True)
result = score[:k]
print(min(result))
