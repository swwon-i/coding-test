def move(command, coord):
    to_coord = [0,0]
    if command == 'U' and coord[1] != 5:
        to_coord[1] = 1
    elif command == 'D' and coord[1] != -5:
        to_coord[1] = -1
    elif command == 'L' and coord[0] != -5:
        to_coord[0] = -1
    elif command == 'R' and coord[0] != 5:
        to_coord[0] = 1
    
    for i in range(2):
        to_coord[i] += coord[i]
    return to_coord

def solution(dirs):
    answer = 0
    visited = set()
    from_coord = [0,0]
    
    for x in dirs:
        to_coord = move(x, from_coord)
        if from_coord == to_coord:
            continue
        test = [0,0]
        for i in range(2):
            test[i] = (from_coord[i] + to_coord[i]) / 2
        visited.add(tuple(test))
        from_coord = to_coord
        
    answer = len(visited)
    return answer