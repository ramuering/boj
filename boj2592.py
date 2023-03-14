arr = set()
brr = []

for i in range(10):
    num = int(input())
    brr.append(num)
    arr.add(num)

temp = 0
for i in arr:
    if temp < brr.count(i):
        temp = brr.count(i)
        result = i
print(sum(brr)//10)
print(result)
