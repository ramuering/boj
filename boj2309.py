import itertools

height = [int(input()) for _ in range(9)]

# 해당 배열에서(height) 7명을 중복없이 뽑아줌
for i in itertools.combinations(height, 7):
    # 합이 100일 때
    if sum(i) == 100:
        # 해당 리스트 오름차순 정렬
        for j in sorted(i):
            print(j)
        break
