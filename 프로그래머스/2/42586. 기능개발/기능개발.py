from collections import deque

def solution(progresses, speeds):
    q = deque(zip(progresses, speeds))
    answer = []
    while q:
        cnt = 0
        p, s = q.popleft()
        days = -(-((100 - p)) // s)  # math.ceil 대신 정수 나눗셈
        cnt += 1
        while q and q[0][0] + q[0][1]*days >= 100:
            q.popleft()
            cnt += 1
        answer.append(cnt)
    return answer