def solution(n, k, cmd):
    deleted = []
    up = [ (i-1) for i in range(n+2)]
    down = [ (i+1) for i in range(n+1)]
    
    k += 1
    
    for cd in cmd:
        if cd.startswith('C'):
            deleted.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k]
            
        elif cd.startswith('Z'):
            restore = deleted.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore
        
        else:
            action, num = cd.split()
            if action == 'U':
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):
                    k = down[k]
    
    answer = ["O"]*n
    for i in deleted:
        answer[i-1] = 'X'
    return "".join(answer)