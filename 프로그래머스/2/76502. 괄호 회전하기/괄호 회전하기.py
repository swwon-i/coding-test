def solution(s):
    n = len(s)
    answer = 0
    sheet = {'[':']', '{':'}', '(':')'}
    
    for i in range(n):
        stack = []

        for j in range(n):
            item = s[(i+j) % n]
            if stack == []:
                if item in [']', '}', ')']:
                    break
                else:
                    stack.append(item)
            else:      
                target = stack[-1]
                if item == sheet[target]:
                    stack.pop()
                elif item in ['[', '{', '(']:
                    stack.append(item)
                else:
                    break
        else:
            if stack == []:
                answer += 1

    return answer