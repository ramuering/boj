array = list(map(int, input().split()))
array.pop(array.index(max(array)))
array.pop(array.index(min(array)))
print(array[0])
