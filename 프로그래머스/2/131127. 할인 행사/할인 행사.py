from collections import defaultdict
def solution(want, number, discount):
    answer = 0
    n = len(want)
    goal = { want[i] : number[i] for i in range(n)}
    m = len(discount)
    
    for i in range(m):
        ans = defaultdict(int)
        for j in range(i, i+10):
            if j < m:
                ans[discount[j]] += 1
            else:
                break
        for obj, num in goal.items():
            if ans.get(obj,0) != num:
                break
        else:
            answer += 1
            
    return answer