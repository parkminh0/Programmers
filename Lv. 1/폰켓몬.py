def solution(nums):
    answer = 0 
    nums.sort()
    tmp = []
    for i in nums:
        if i not in tmp:
            tmp.append(i)
    if len(tmp) > len(nums)/2:
        return len(nums)/2
    return len(tmp)