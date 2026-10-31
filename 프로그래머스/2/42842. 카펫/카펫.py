
def solution(brown, yellow):
    answer = []
    limit = int(yellow**0.5)
    for x in range(1, limit+1):
        if yellow % x == 0:
            y = yellow / x
            if 2*(x+2)+2*(y+2) == brown+4:
                answer = [x+2,y+2]
    answer.sort()
    answer.reverse()
    return answer