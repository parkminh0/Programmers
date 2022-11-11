def solution(sizes):
    tmp = []
    for i in sizes:
        i.sort()
        tmp.append(i)
    tmp.sort()
    x = tmp[-1][0]
    
    sizes = sorted(sizes, key = lambda x : x[1])
    y = sizes[-1][1]
    return x*y