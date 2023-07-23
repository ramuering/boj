def solution(lines):
    ans=0
    chk=[0]*201
    for i in range(len(lines)):
        for j in range(lines[i][0],lines[i][1]):
            chk[j+100]+=1
    for i in range(len(chk)):
        if chk[i]>1:
            ans+=1
        
                    
                    
    return ans