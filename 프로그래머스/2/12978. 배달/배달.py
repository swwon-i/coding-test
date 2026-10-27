import heapq
def solution(N, road, K):
    graph = [ [] for _ in range(N+1)]
    dists = [float('inf')]*(N+1)
    dists[1] = 0
    
    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
        
    heap = []
    heapq.heappush(heap, (0,1))
    while heap:
        dist, node = heapq.heappop(heap)
        
        for next_node, next_dist in graph[node]:
            cost = dist + next_dist
            if cost < dists[next_node]:
                dists[next_node] = cost
                heapq.heappush(heap, (cost, next_node))
    
    

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return sum(1 for x in dists if x <= K)