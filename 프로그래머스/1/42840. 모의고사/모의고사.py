def solution(answers):
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    a = [a1,a2,a3]
    score = [0,0,0]
    n = len(answers)
    for i in range(n):
        for j in range(3):
            if answers[i] == a[j][i % len(a[j])]:
                score[j] += 1
            
    max_score = max(score)
    
    answer = []
    l = len(score)
    for idx in range(l):
        if score[idx] == max_score:
            answer.append(idx+1)
    
    return answer