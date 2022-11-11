def solution(a, b):
    answer = ''
    DAY = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    DAYS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    days = b
    for i in range(a-1):
        days += DAYS[i]
        
    return DAY[days%7]