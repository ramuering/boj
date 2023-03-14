score = []
result = []
for _ in range(8):
    score.append(int(input()))
high = sorted(score)
for num in high[3:]:
    result.append(str((score.index(num))+1))
r = sorted(result)
print(sum(high[3:]))
print(' '.join(r))
