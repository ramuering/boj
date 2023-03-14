t = int(input())
ox = [0]*2
for i in range(t):
    ans = int(input())
    ox[ans] += 1

if ox[0] > ox[1]:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
