from math import gcd
def factor(x):
    chk=2
    while chk<=x:
        if x%chk==0:
            x=x//chk
            if chk!=2 and chk!=5:
                return 2
        else:
            chk+=1
    return 1
def solution(a, b):
    n=gcd(a,b)
    b=b//n
    
    return factor(b)
