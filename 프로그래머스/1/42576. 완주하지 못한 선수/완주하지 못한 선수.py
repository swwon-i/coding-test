from collections import defaultdict
def solution(participant, completion):
    dic = defaultdict(int)
    answer = ''
    
    for x in participant:
        dic[x] += 1
    for x in completion:
        dic[x] -= 1
        
    for x,y in dic.items():
        if y == 1:
            answer = x
            break
            
    return answer