def solution(id_list, report, k):
    reporting = {}
    reported = {}
    answer = [0]*len(id_list)
    for user in id_list:
        reporting[user] = set([])
        reported[user] = 0
        
    for event in report:
        x,y = event.split()
        if y not in reporting[x]:
            reported[y] += 1
            reporting[x].add(y)
        
    report_list = set([])
    for user, num in reported.items():    
        if num >= k:
            report_list.add(user)
    
    for i in range(len(id_list)):
        temp = reporting[id_list[i]].intersection(report_list)
        answer[i] += len(temp)
        
    return answer