from collections import defaultdict

def solution(record):
    answer = []
    ans = []    
    man = defaultdict(str)
    
    for x in record:
        step = x.split(" ")
        ans.append((step[0], step[1]))
        if step[0] != "Leave":
            man[step[1]] = step[2]
        
    for step in ans:    
        command = step[0]
        user_id = step[1]
        if command == 'Enter':
            temp = man[user_id] + "님이 들어왔습니다."
            answer.append(temp)
        elif command == 'Leave':
            temp = man[user_id] + "님이 나갔습니다."
            answer.append(temp)
    
    return answer