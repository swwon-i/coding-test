def solution(cards1, cards2, goal):
    ans = []
    id1 = 0
    id2 = 0
    
    for x in goal:
        if id1 < len(cards1) and cards1[id1] == x:
            id1 += 1
        elif id2 < len(cards2) and cards2[id2] == x:
            id2 += 1
        else:
            return 'No'
    else:
        return 'Yes'
    return answer