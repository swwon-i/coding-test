import heapq

def sol(start, end, board, maps, heap):
    n = len(maps)
    for x1, y1, how1 in [(1,0,1), (0,1,-1)]:
        if board[x1][y1] == 0:
            maps[x1][y1][how1] = 100
            heapq.heappush(heap, (100, x1, y1, how1))
    
    while heap:
        cost, x, y, how = heapq.heappop(heap)
        for x1, y1, how1 in [(x-1,y,1), (x+1,y,1), (x,y-1,-1), (x,y+1,-1)]:
            if 0 <= x1 < n and 0 <= y1 < n and board[x1][y1] == 0:
                if how * how1 == 1:
                    if min(maps[x1][y1][how1], cost + 100) == cost + 100:
                        maps[x1][y1][how1] = cost+100
                        heapq.heappush(heap, (maps[x1][y1][how1],x1,y1,how1))
                elif how * how1 == -1:
                    if min(maps[x1][y1][how1], cost + 600) == cost + 600:
                        maps[x1][y1][how1] = cost+600
                        heapq.heappush(heap, (maps[x1][y1][how1],x1,y1,how1))
    return min(maps[n-1][n-1])

def solution(board):
    n = len(board)
    start = (0,0)
    end = (n-1, n-1)
    heap = []
    maps = [[[float('inf')]*3 for _ in range(n)] for _ in range(n)]
    maps[0][0] = [0, 0, 0] 
    
    return sol(start, end, board, maps, heap)