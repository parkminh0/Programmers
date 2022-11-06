def solution(denum1, num1, denum2, num2):
    answer = [denum1*num2 + denum2*num1,num1*num2]
    div = 2
    while div <= min(answer[0], answer[1]):
        if answer[0] % div == 0 and answer[1] % div == 0:
            answer = [answer[0]//div, answer[1]//div]
        else: 
            div += 1
    
    return answer