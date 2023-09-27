board = list(input())
ans = []
# 임시 리스트
tmp = []

for i in range(len(board)):
    # 이번에 들어오는 보드가 0일때
    if board[i] == '.':
        # tmp에 들은 x가 짝수개라면
        if len(tmp) % 2 == 0 and len(tmp) > 0:
            ans.append('BB')
            tmp = []
        # 1개 들어있는 상태로 .을 만나면 보드를 채울 수 없다(X.X 경우)
        elif len(tmp) % 2 != 0:
            print(-1)
            exit(0)
        ans.append('.')
    else:
        tmp.append(board[i])
        # 사전순으로 앞서야하기때문에 BB는 위에서 AAAA는 여기서 처리
        if len(tmp) % 4 == 0 and len(tmp) > 0:
            ans.append('AAAA')
            tmp = []
# 마지막 루프에서 더해진 tmp 변환 처리
if len(tmp) % 2 == 0 and len(tmp) > 0:
    ans.append('BB')
    tmp = []

if len(tmp) > 0:
    print(-1)
else:
    print(''.join(ans))
