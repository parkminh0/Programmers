import math
def solution(nums):
    answer = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                x = nums[i] + nums[j] + nums[k]
                cnt = 2
                sosu = True
                while cnt <= int(math.sqrt(x)):
                    if x % cnt == 0:
                        sosu = False
                        break
                    cnt += 1
                if sosu == True:
                    answer += 1
    return answer