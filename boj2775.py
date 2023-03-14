t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    apt = [[0]*15 for _ in range(k+1)]
    apt[0] = [i for i in range(15)]
    for i in range(1, k+1):
        result = [0]*15
        for j in range(1, 15):
            result[j] = apt[i-1][j]+result[j-1]
        apt[i] = [num for num in result]
    print(apt[k][n])
