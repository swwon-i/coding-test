from collections import defaultdict
def solution(want, number, discount):
    answer = 0
    n = len(want)
    m = len(discount)
    goal = { want[i] : number[i] for i in range(n)}
    
    day = 0
    
    window = defaultdict(int)
    for j in range(10):              
        window[discount[j]] += 1
    
    for i in range(m - 9):
        if i > 0:                     
            window[discount[i - 1]] -= 1
            window[discount[i + 9]] += 1
        
        for obj, num in goal.items():
            if window.get(obj, 0) != num:
                break
        else:
            answer += 1
    
    return answer