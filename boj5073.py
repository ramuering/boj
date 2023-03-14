while True:
    arr = list(map(int, input().split()))
    if sum(arr) == 0:
        break
    result = set(arr)
    arr.sort(reverse=True)
    if arr[0] >= arr[1]+arr[2]:
        print("Invalid")
    else:
        if len(result) == 3:
            print("Scalene")
        if len(result) == 2:
            print("Isosceles")
        if len(result) == 1:
            print("Equilateral")
