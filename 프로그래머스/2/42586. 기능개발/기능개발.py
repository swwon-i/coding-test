from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    idx = 0
    
    while idx <= n-1:
        ans = 0
        days = math.ceil((100 - progresses[idx]) / speeds[idx])
        for i in range(idx, n):
            progresses[i] += speeds[i]*days
        while True:
            if idx <= n-1 and progresses[idx] >= 100:
                idx += 1
                ans += 1
            else:
                answer.append(ans)
                break
        
    return answer