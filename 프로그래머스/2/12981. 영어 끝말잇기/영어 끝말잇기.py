def solution(n, words):
    m = len(words)
    word = set()
    word.add(words[0])
    for i in range(1, m):
        if words[i] not in word and words[i-1][-1] == words[i][0]:
            word.add(words[i])
        else:
            a = (i % n) + 1
            b = (i // n) + 1
            return [a,b]
    return [0,0]            

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

