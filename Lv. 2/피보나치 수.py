def solution(n):
    piv = [0, 1]
    answer = 0
    for i in range(1, n):
        piv.append(piv[-1] + piv[-2])
        
    return piv[-1]%1234567