from collections import Counter

def solution(topping):
    right = Counter(topping)      # 동생 쪽: 처음엔 케이크 전부
    left = set()                  # 철수 쪽: 처음엔 비어 있음
    answer = 0
    for t in topping[:-1]:        # 자르는 위치를 한 칸씩 오른쪽으로
        left.add(t)               # t가 철수 쪽으로 넘어감
        right[t] -= 1
        if right[t] == 0:         # 동생 쪽에 t가 더 없으면 종류에서 제거
            del right[t]
        if len(left) == len(right):
            answer += 1
    return answer