def solution(hp):
    answer = 0
    if hp // 5 >= 1:
        answer += hp // 5
        hp %= 5
    if hp // 3 >= 1:
        answer += hp // 3
        hp %= 3
    answer += hp
    return answer