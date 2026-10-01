def solution(numbers):
    
    n = len(numbers)
    ans_set = set()
    
    for i in range(n-1):
        for j in range(i+1, n):
            temp = numbers[i] + numbers[j]
            ans_set.add(temp)
        
    answer = list(ans_set)
    answer.sort()
    
    return answer