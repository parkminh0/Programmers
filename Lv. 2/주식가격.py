def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        x = prices[i]
        cnt = 0
        hi = True
        for j in range(i+1, len(prices)):
            if x <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    answer.append(0)
    return answer