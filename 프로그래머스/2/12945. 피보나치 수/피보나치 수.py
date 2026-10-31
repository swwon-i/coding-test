def sol(n):
    answer = [0,1]
    for x in range(1,n):
        answer.append(answer[-2]+answer[-1])
    return answer[-1]
def solution(n):
    
    return sol(n) % 1234567