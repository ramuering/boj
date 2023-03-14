n, m = map(int, input().split())
basket = [x for x in range(n+1)]

for t in range(m):
    i, j, k = map(int, input().split())
    stop = k
    temp = []
    for c in range(k, j+1):
        temp.append(basket[c])
    for r in range(i, k):
        temp.append(basket[r])
    basket[i:j+1] = temp
basket.pop(0)
for i in basket:
    print(i, end=' ')
