from collections import deque

def sol(start, end, maps):
    x,y = start[0], start[1]
    que = deque([(x,y,1)])
    visit = set([(x,y)])
    n = len(maps)
    m = len(maps[0])
    while que:
        x,y,t = que.popleft()
        for x_,y_ in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
            if 0 <= x_ < n and 0 <= y_ < m and (x_,y_) not in visit:  
                if (x_,y_) == end:
                    return t+1
                if maps[x_][y_] == 1:
                    visit.add((x_,y_))
                    que.append((x_,y_,t+1))
                
    return -1

def solution(maps):
    start = (0,0)
    n = len(maps)
    m = len(maps[0])
    end = (n-1, m-1)
    answer = sol(start, end, maps)
    
    return answer