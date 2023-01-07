# N × M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하라.

def dfs(x, y):

    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if graph[x][y] == 0 and visited[x][y] == False:
        visited[x][y] = True
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x-1, y)
        dfs(x+1, y)

        return True

    return False

n,m = map(int, input().split())
graph = []

#좌표 입력받기
for __ in range(n):
    graph.append(list(map(int, input())))

#방문여부 리스트 생성
visited = []
for _ in range(n):
    visited.append([False for __ in range(m)])

cnt = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            print(i,j)
            cnt += 1

print(cnt)


