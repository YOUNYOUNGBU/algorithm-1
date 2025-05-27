from collections import deque

# DFS 구현 (재귀)
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for neighbor in sorted(graph[v]):
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

# BFS 구현 (큐)
def bfs(graph, start):
    visited = [False] * (len(graph))
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for neighbor in sorted(graph[v]):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# 입력 처리
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 출력
visited_dfs = [False] * (n + 1)
dfs(graph, v, visited_dfs)
print()

# BFS 출력
bfs(graph, v)
