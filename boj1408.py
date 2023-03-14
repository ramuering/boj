# 시간 : 기준으로 분리
t = list(map(int, input().split(":")))
st = list(map(int, input().split(":")))
# 시작 시간 st 에서 현재 시간 t 빼기
# 1시간 =3600초 , 1분 =60초
re = (st[0]*3600+st[1]*60+st[2]) - (t[0]*3600+t[1]*60+t[2])
# 시각이 음수일 경우 24시간(86400초) 더하기
if re < 0:
    re += 86400
# 1시간(3600초)로 시각 분리 후 나머지 b저장
a, b = divmod(re, 3600)
# 1분(60초)로 분 분리 후 나머지 초 저장
c, d = divmod(b, 60)
# zfill 함수로 0채워 두자리 수 맞추기
print("{}:{}:{}".format(str(a).zfill(2), str(c).zfill(2), str(d).zfill(2)))
