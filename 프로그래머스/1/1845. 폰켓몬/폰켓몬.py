def solution(nums):
    n = len(nums)
    take = n / 2
    num_set = set(nums)
    m = len(num_set)
    
    answer = 0
    if take < m:
        answer = take
    else:
        answer = m
    
    return answer