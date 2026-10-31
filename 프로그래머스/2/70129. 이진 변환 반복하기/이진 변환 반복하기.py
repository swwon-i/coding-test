def sol2(s):
    x = len(s)
    ans = []
    while x >= 1:
        ans.append(str(x % 2))
        x = x // 2
    ans.reverse()
    return ''.join(ans)
    
def sol(n,s):
    new_s = ''
    for x in s:
        if x == '0':
            n += 1
        else:
            new_s += x
    return n, sol2(new_s)

def solution(s):
    n = 0
    answer = [0, 0]
    
    while s != '1':
        n, s = sol(n,s)
        answer[0] += 1
    answer[1] = n
    return answer