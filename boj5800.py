t = int(input())
for i in range(t):
    score = list(map(int, input().split()))
    score.pop(0)
    score.sort(reverse=True)
    gap = 0
    for n in range(len(score)):
        if n+1 == len(score):
            break
        if score[n]-score[n+1] > gap:
            gap = score[n]-score[n+1]
    print("Class", i+1)
    print("Max {}, Min {}, Largest gap {}".format(
        max(score), min(score), gap))
