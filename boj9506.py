while True:
    num = int(input())
    if num == -1:
        break
    array = []
    max = 0
    for i in range(1, num):
        if num % i == 0:
            if max == i:
                break
            array.append(i)
            j = num//i
            if j == num:
                continue
            else:
                array.append(j)
                max = j

    array.sort()
    print(num, end=" ")
    if num == sum(array):
        for i in array:
            if i == 1:
                print("=", i, end="")
            else:
                print(" +", i, end="")
        print("")
    else:
        print("is NOT perfect.")
