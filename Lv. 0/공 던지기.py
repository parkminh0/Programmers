def solution(numbers, k):
    numbers *= 10000
    return numbers[k*2-2]