def solution(score):
    tmp=[]
    vis=[]
    for a,b in score:
        tmp.append(a+b)
    ans=list(set(tmp))
    ans=sorted(ans, reverse=True)
    rank=1
    cnt=0
    print(ans)
    print(tmp)
    for s in ans:
        rank+=cnt
        cnt=0
        for j in range(len(tmp)):
            if s==tmp[j] and j not in vis:
                tmp[j]=rank
                vis.append(j)
                cnt+=1
    print(tmp)
    return tmp