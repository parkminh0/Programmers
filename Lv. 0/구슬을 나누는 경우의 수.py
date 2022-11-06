def solution(balls, share):
    top = 1
    bottom = 1
    for i in range(share):
        top *= balls
        bottom *= share
        balls -= 1
        share -= 1
    
    return top / bottom