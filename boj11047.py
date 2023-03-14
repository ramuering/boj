n, k = map(int, input().split())

won = []
for _ in range(n):
    won.append(int(input()))
won.reverse()
a = [0]*(max(won)+1)
for i in won:
    while k-i >= 0:
        k -= i
        a[i] += 1
print(sum(a))
