def solution(land):
    answer = 0
    n = len(land)
    dp = land.copy()
    
    for i in range(1, n):
        for j in range(4):
            ans = []
            for m in range(4):
                if j != m:
                    ans.append(land[i-1][m])
            dp[i][j] += max(ans)
            
    return max(dp[-1])
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer