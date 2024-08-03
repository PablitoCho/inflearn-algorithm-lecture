maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]] # -1

# 프로그래머스, 깊이/너비 우선 탐색(DFS/BFS) > 게임 맵 최단거리
from collections import deque

visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
distances = [[-1 for _ in range(len(maps[0]))] for _ in range(len(maps))]
q = deque()

q.append((0, 0))
# print(visited)
visited[0][0] = True
distances[0][0] = 1
# path = [(0,0)]
while q:
    x, y = q.popleft()
    # print(f'x {x}, y {y} path {path}')
    # maps[y][x]
    for dy, dx in [[1,0], [-1,0],[0,1],[0,-1]]:
        ny = y + dy
        nx = x + dx
        if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps):
            if maps[ny][nx] == 1 and not visited[ny][nx]:
                q.append((nx, ny))
                visited[ny][nx] = True
                distances[ny][nx] = distances[y][x] + 1
                # path.append((nx, ny))

print(distances[len(maps)-1][len(maps[0])-1])