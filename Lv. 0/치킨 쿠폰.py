def solution(chicken):
    service = chicken // 10
    coupon = service + chicken % 10
    tmp = [service]
    while True:
        if coupon < 10:
            break
        service = coupon // 10
        coupon = service + coupon % 10
        tmp.append(service)
    return sum(tmp)