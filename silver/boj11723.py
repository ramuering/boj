import sys

result = 0
all = (1 << 20)-1  # 0번부터 19번째 자릿수 만큼 1로 채우기
for _ in range(int(sys.stdin.readline())):
    arr = list(sys.stdin.readline().split())
    if len(arr) == 2:
        arr[1] = int(arr[1])-1  # 0부터19번까지 사용하지만 문제에서 1-20을 사용하기 떄문에 -1해줌

    if arr[0] == 'add':
        result |= 1 << arr[1]  # 1) or 연산
    elif arr[0] == 'remove':
        result &= ~(1 << arr[1])  # 2) and 연산
    elif arr[0] == 'check':
        print(1 if result & (1 << arr[1]) else 0)
    elif arr[0] == 'toggle':
        result ^= 1 << arr[1]  # 3) xor 연산
    elif arr[0] == 'all':
        result = all
    else:
        result = 0
