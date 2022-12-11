def solution(arr):
    div = 1
    while True:
        chk = 0
        for i in arr:
            if div % i == 0:
                chk += 1
        if chk == len(arr):
            return div
        div += 1