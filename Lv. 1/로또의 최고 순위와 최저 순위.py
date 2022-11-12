def solution(lottos, win_nums):
    answer = []
    rank = [-1, 6, 5, 4, 3, 2, 0]
    cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
            
    if cnt < 2:
        tmp = [cnt+lottos.count(0), 0]
        if cnt + lottos.count(0) < 2:
            tmp = [0, 0]
    else:
        tmp = [cnt+lottos.count(0), cnt]
        
    answer.append(rank.index(tmp[0]))
    answer.append(rank.index(tmp[1]))
    return answer