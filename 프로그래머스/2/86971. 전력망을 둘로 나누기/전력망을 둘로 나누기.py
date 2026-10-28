from collections import defaultdict

def sol(n, tree, wires):
    ans = []
    for target in range(1, n+1):
        answer = 1
        visited = set([1,target])
        stack = [1]
        while stack:
            node = stack.pop()
            for to_node in tree[node]:
                if to_node not in visited:
                    visited.add(to_node)
                    stack.append(to_node)
                    answer += 1
        ans.append(abs(answer-(n-answer)))
    return min(ans)
            
def solution(n, wires):
    tree = defaultdict(list)
    for a,b in wires:
        tree[a].append(b)
        tree[b].append(a)
        
    
    return sol(n, tree, wires)