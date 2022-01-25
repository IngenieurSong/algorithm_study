from collections import deque
import copy

def dfs_0(v, graph):
    stack = deque([])
    stack.append(v)
    answer = ""

    while(stack):
        node = stack.pop()

        for i in range(2):
            if(graph[node][-1 - i] != '.'):
                stack.append(graph[node][-1 - i])
                graph[node][-1 - i] = '.'

        answer += node

    return answer

def dfs_1(v, graph):
    stack = deque([])
    stack.append(v)
    answer = ""

    while(stack):
        node = stack.pop()

        if(graph[node][0] == '.' and graph[node][1] == '.'):
            answer += node

        else:
            if(graph[node][1] != '.'):
                stack.append(graph[node][1])
                graph[node][1] = '.'

            stack.append(node)

            if(graph[node][0] != '.'):
                stack.append(graph[node][0])
                graph[node][0] = '.'

    return answer

def dfs_2(v, graph):
    stack = deque([])
    stack.append(v)
    answer = ""

    while(stack):
        node = stack.pop()

        if(graph[node][0] == '.' and graph[node][1] == '.'):
            answer += node
        else:
            stack.append(node)

            for i in range(2):
                if(graph[node][-1 - i] != '.'):
                    stack.append(graph[node][-1 - i])
                    graph[node][-1 - i] = '.'

    return answer

n = int(input())
graph = {}

for _ in range(n):
    key, value1, value2 = map(str, input().split())

    graph[key] = [value1, value2]

graph0 = copy.deepcopy(graph)
graph1 = copy.deepcopy(graph)
graph2 = copy.deepcopy(graph)

print(dfs_0('A', graph0))
print(dfs_1('A', graph1))
print(dfs_2('A', graph2))
