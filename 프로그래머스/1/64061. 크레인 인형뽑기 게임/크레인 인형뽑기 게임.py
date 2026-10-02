def sol(stack, num, answer):
    if stack and stack[-1] == num:
        answer += 2
        stack.pop()
    else:
        stack.append(num)
    return answer

def solution(board, moves):
    n = len(board)
    answer = 0
    stack = []
    
    for x in moves:
        for i in range(n):
            if board[i][x-1] != 0:
                doll = board[i][x-1]
                board[i][x-1] = 0
                answer = sol(stack, doll, answer)
                break
    return answer

#   1 2 3 4 5
# [[0,0,0,0,0],
#  [0,0,1,0,3],
#  [0,2,5,0,1],
#  [4,2,4,4,2],
#  [3,5,1,3,1]]


