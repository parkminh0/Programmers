def solution(numbers, hand):
    answer = ''
    left = [1, 4, 7]
    right = [3, 6, 9]
    mid = [2, 5, 8, 0]
    pad = [[1, 2, 3],[4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    l = [3, 0]
    r = [3, 2]
    
    for i in numbers:
        for j in range(4):
            for k in range(3):
                if pad[j][k] == i and i in left:
                    l = [j, k]
                    answer += 'L'  
                elif pad[j][k] == i and i in right:
                    r = [j, k]
                    answer += 'R'
                elif pad[j][k] == i and i in mid:
                    l_cnt = abs(l[0]-j)+abs(l[1]-k)
                    r_cnt = abs(r[0]-j)+abs(r[1]-k)
                    if l_cnt < r_cnt:
                        l = [j, k]
                        answer += 'L'  
                    elif l_cnt > r_cnt:
                        r = [j, k]
                        answer += 'R'
                    elif l_cnt == r_cnt:
                        if hand == 'left':
                            l = [j, k]
                            answer += 'L'
                        else:
                            r = [j, k]
                            answer += 'R'
    return answer