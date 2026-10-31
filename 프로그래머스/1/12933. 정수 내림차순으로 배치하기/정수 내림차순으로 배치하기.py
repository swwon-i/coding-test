def solution(n):
    
    num = str(n)
    num = list(sorted(num, key=lambda x: x, reverse=True))
    answer = int(''.join(num))
    return answer