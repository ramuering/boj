n = int(input())
d = list(map(int, input().split()))
c = list(map(int, input().split()))

cost = 0
tmp = []
for i in range(len(d)):
    tmp.append(c[i])
    cost += min(tmp)*d[i]

print(cost)
