from collections import defaultdict

def sol(i, computer, visit, tree):
    stack = [i]
    while stack:
        idx = stack.pop()
        visit[idx] = True
        for x in tree[idx]:
            if visit[x] == False:
                visit[x] == True
                stack.append(x)
    
def solution(n, computers):
    answer = 0
    visit = [False] * n
    tree = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                tree[i].append(j)
    
    for i in range(n):
        if visit[i] == False:
            answer += 1
            sol(i, computers, visit, tree)
    
    return answer