# 깊이 우선 탐색(DFS, Depth-First Search)이란? 
그래프나 트리 자료 구조를 탐색하는 알고리즘 중 하나.

DFS는 한 노드에서 시작하여 최대한 깊이 내려간 후, 더 이상 진행할 수 없으면 다시 돌아와서 탐색을 이어가는 방식.

## (1) DFS 동작 방식
1. 시작 노드를 방문

2. 방문한 노드를 스택에 저장

3. 방문한 노드의 인접 노드를 확인

4. 아직 방문하지 않은 노드가 있으면 깊이 이동

5. 더 이상 이동할 곳이 없으면 뒤로 돌아감

6. 모든 노드를 방문할 때까지 반복

## (2) DFS 예제 (Python 코드)
<pre>
  <code>
    graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# DFS 구현 (재귀 방식)
def dfs(node, visited=set()):
    if node not in visited:
        print(node, end=" ")  # 방문한 노드 출력
        visited.add(node)  # 방문 처리
        for neighbor in graph[node]:  # 인접 노드 방문
            dfs(neighbor, visited)

# 탐색 실행
dfs('A')
  </code>
</pre>

## 결과 
A B D E C F 위 코드는 A 노드부터 깊이 우선 탐색을 진행하여 모든 노드를 탐색.

## (3) DFS의 특징
1. 백트래킹(Backtracking) 방식으로 탐색
   
2. 메모리 사용량이 적음 (탐색 경로만 저장)
   
3. 경로가 깊은 그래프에 적합
   
4. 무한 루프에 빠지지 않도록 방문 여부 체크 필수
