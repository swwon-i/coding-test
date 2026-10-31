def sol(n):
    answer = [1,2]
    for i in range(2,n):
        answer.append((answer[-2]+ answer[-1])% 1000000007)
    return answer[-1]

def solution(n):
    
    return sol(n) 