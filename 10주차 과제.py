# 노드 개수(n)
n = 6

# 에지 5개. 간선 정보 (무방향 그래프)
m = [
    (1, 2),
    (2, 5),
    (5, 1),
    (3, 4),
    (4, 6)
]

# 인접 리스트 초기화 
A = [[] for _ in range(n + 1)]

# 방문 기록 리스트 초기화
visited = [False] * (n + 1)

# 그래프 데이터 저장
for u, v in m:
    A[u].append(v)
    A[v].append(u)

# DFS 함수
def dfs(node):
    visited[node] = True
    for neighbor in A[node]:
        if not visited[neighbor]:
            dfs(neighbor)

# 연결 요소 개수 세기
count = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1

# 결과 출력
print("연결 요소 개수:", count)
