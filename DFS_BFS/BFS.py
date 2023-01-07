from collections import deque

#BFS 메서드
def bfs(graph, started, visited):
    queue = deque([started])
    visited[started] = True
    #큐가 빌 때까지 반복함.
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        #해당 노드와 연결된 모든 노드를 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

#그래프를 인접 리스트로 표현
graph = [[], [2,3,8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

#방문 여부 리스트
visited = [False] * 9

bfs(graph, 1, visited)
