from collections import deque

def sol(L, maps):
    x,y = L[0], L[1]
    n = len(maps)
    m = len(maps[0])
    visited = set((x,y))
    S_time = 0
    E_time = 0
    que = deque()
    que.append([x,y,0])
    while que:
        x,y,t = que.popleft()
        
        for x_, y_ in [(x-1,y), (x+1,y), (x,y-1),(x,y+1)]:
            if 0 <= x_ < n and 0 <= y_ < m and maps[x][y] != 'X':
                if (x_,y_) not in visited:
                    visited.add((x_,y_))
                    que.append((x_,y_,t+1))
                if maps[x][y] == "S":
                    S_time = t
                elif maps[x][y] == "E":
                    E_time = t
    
    if S_time == 0 or E_time == 0:
        return -1
    else:
        return S_time + E_time

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dic = {"S":(0,0), "L":(0,0), "E":(0,0)}
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                dic["S"] = (i,j)
            elif maps[i][j] == "L":
                dic["L"] = (i,j)
            elif maps[i][j] == "E":
                dic["E"] = (i,j)
                
    
    answer = sol(dic["L"],maps)
    return answer