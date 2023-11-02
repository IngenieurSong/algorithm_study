def travel(dirs, vector, x, y):
    roads = set()

    for i in dirs:
        nx = x + vector[i][0]
        ny = y + vector[i][1]

        if(nx < -5 or nx > 5 or ny < -5 or ny > 5):
            continue

        roads.add(((x, y), (nx, ny)))
        roads.add(((nx, ny), (x, y)))

        x = nx
        y = ny

    return len(roads) // 2

def solution(dirs):
    vector = {'U' : (0, 1), 'D' : (0, -1), 'R' : (1, 0), 'L' : (-1, 0)}

    result = travel(dirs, vector, 0, 0)
    return result
