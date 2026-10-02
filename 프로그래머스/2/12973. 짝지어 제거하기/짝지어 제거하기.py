def solution(s):
    
    ans = []
    for c in s:
        if ans and ans[-1] == c:
            ans.pop()
        else:
            ans.append(c)
    
    return int(not ans)
    