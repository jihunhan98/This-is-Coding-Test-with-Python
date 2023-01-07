# N x M 크기의 직사각형 형태의 미로에 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다.
# 현재 위치는 (1, 1)이고 미로의 출구는 (N,M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다.
# 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다.
# 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하라. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

def bfs(x, y):
    if x < 0 or y < 0 or x >= m or y >= n:
        return False

    if graph[x][y] == 1:

        bfs(x, y+1)
        bfs(x+1, y)





n, m = map(int, input().split())
graph = []

for _ in range(m):
    graph.append(list(map(int, input())))

for i in range(m):
    for j in range(n):
        bfs(i, j)