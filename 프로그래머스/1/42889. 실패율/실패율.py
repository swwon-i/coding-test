def solution(N, stages):
    answer = []
    ans = {}
    
    for i in range(1, N+1):
        n_man = 0
        s_man = 0
        for stage in stages:
            if stage >= i:
                s_man += 1
            if stage == i:
                n_man += 1
        ans[i] = n_man / s_man if s_man != 0 else 0
    answer = sorted(ans, key = lambda x:ans[x], reverse=True)
    return answer