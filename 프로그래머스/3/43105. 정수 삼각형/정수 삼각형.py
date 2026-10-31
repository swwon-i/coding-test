def solution(triangle):
    answer = 0
    n = len(triangle)
    ans = triangle.copy()
    
    for i in range(1,n):
        for j in range(len(ans[i])):
            if j == 0:
                ans[i][j] += ans[i-1][0]
            elif j == i:
                ans[i][j] += ans[i-1][i-1]
            else:
                ans[i][j] = max(ans[i-1][j-1], ans[i-1][j]) + triangle[i][j]
    
    return max(ans[-1])