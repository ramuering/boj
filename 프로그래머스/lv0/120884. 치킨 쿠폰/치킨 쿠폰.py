def solution(chicken):
    ans=0
    coupon=chicken
    while True:
        ans+=(coupon//10)
        tmp=coupon//10
        coupon%=10
        coupon+=tmp
        if coupon<10:
            break
    return ans