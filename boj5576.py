arr = []
brr = []
for _ in range(10):
    arr.append(int(input()))
for _ in range(10):
    brr.append(int(input()))
arr.sort(reverse=True)
brr.sort(reverse=True)
print(sum(arr[:3]), sum(brr[:3]))
