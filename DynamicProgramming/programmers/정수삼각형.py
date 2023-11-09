inf = int(1e9)

def solution(triangle):
    cache = []
    for i in range(1, len(triangle) + 1, 1):
        cache.append([-inf] * i)

    cache[0][0] = triangle[0][0]

    for i in range(len(triangle) - 1):
        for j in range(i + 1):
            cache[i + 1][j] = max(cache[i + 1][j], cache[i][j] + triangle[i + 1][j])
            cache[i + 1][j + 1] = max(cache[i + 1][j + 1], cache[i][j] + triangle[i + 1][j + 1])

    return max(cache[len(triangle) - 1])
