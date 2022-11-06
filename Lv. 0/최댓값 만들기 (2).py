def solution(numbers):
    result = numbers[0] * numbers[1]
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i] * numbers[j] > result:
                result = numbers[i] * numbers[j]
    return result