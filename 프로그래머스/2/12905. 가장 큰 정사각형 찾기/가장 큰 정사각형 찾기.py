def solution(board):
    answer = 1234
    n = len(board)
    m = len(board[0])

    for i in range(1,n):
        for j in range(1,m):
            if board[i][j] == 1:
                left = board[i][j-1]
                up = board[i-1][j]
                left_up = board[i-1][j-1]
                
                board[i][j] = min(left, up, left_up) + 1
    max_val = max(max(row) for row in board)**2
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return max_val