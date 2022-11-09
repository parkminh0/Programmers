def solution(numbers):
    tmp = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    answer = ''
    test = ''
    for i in numbers:
        test += i
        if test in tmp:
            answer += str(tmp.index(test))
            test = ''
    
    return int(answer)