def solution(n, m, x, y, r, c, k):
    dist = abs(x - r) + abs(y - c)
    # 거리가 k보다 멀거나, 남는 이동이 홀수면 불가능
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"

    moves = [("d", 1, 0), ("l", 0, -1), ("r", 0, 1), ("u", -1, 0)]   # 사전순
    path = []
    for step in range(k):
        remain = k - step - 1                       # 이번 이동 후 남는 횟수
        for ch, dx, dy in moves:
            nx, ny = x + dx, y + dy
            # 격자 안 + 이동 후에도 남은 횟수 안에 도착 가능
            if 1 <= nx <= n and 1 <= ny <= m and abs(nx - r) + abs(ny - c) <= remain:
                path.append(ch)
                x, y = nx, ny
                break                               # 사전순 첫 번째로 확정
    return "".join(path)