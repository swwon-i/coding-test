def solution(keyinput, board):
    answer = [0,0]
    x = board[0] // 2
    y = board[1] // 2
    for word in keyinput:
        if word == "left" and answer[0] > -x:
            answer[0] -= 1
        elif word == "right" and answer[0] < x:
            answer[0] += 1
        elif word == "up" and answer[1] < y:
            answer[1] += 1 
        elif word == "down" and answer[1] > -y:
            answer[1] -= 1
    
    return answer