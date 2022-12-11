from itertools import permutations

def solution(k, dungeons):
    tmp = permutations(dungeons, len(dungeons))
    answer = []
    for i in tmp:
        x = k
        cnt = 0
        for j in i:
            if x >= j[0]:
                x -= j[1]
                cnt += 1
            else:
                break
        answer.append(cnt)
        
    return max(answer)
