def solution(A, B):
    answer = 0
    tmp = []
    A = list(A)
    B = list(B)
    if A == B:
        return 0
    cnt = 1
    while cnt < len(B):
        tmp.append(A[-1])
        for i in range(len(A)-1):
            tmp.append(A[i])
            if tmp == B:
                return cnt
                break
        A = tmp
        tmp = []
        cnt += 1
    return -1