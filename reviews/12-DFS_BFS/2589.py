# https://www.acmicpc.net/problem/2589

H, W = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(H)]
# [
#  ['W', 'L', 'L', 'W', 'W', 'W', 'L'], 
#  ['L', 'L', 'L', 'W', 'L', 'L', 'L'], 
#  ['L', 'W', 'L', 'W', 'L', 'W', 'W'], 
#  ['L', 'W', 'L', 'W', 'L', 'L', 'L'], 
#  ['W', 'L', 'L', 'W', 'L', 'W', 'W']
# ]

from collections import deque

# print(visited)
for y in range(H):
    for x in range(W):
        # print(graph[y][x])
        if graph[y][x] == 'L':
            # 각 'Land'마다 다른 Land들을 대상으로 BFS 수행
            visited = [[0 for _ in range(W)] for _ in range(H)]
            dists = [[0 for _ in range(W)] for _ in range(H)]
            q = deque()
            q.append((y,x)) # 시작점
            visited[y][x] = 1
            max_dist = 0
            print(f'from ({y}, {x})')
            while q:
                _y, _x = q.popleft()
                for dy, dx in [[1,0],[-1,0],[0,1],[0,-1]]:
                    ny = _y + dy
                    nx = _x + dx
                    if (0 <= ny < H) and (0 <= nx < W):
                        if graph[ny][nx] == 'L':
                            # 연결된 이웃 Land
                            if visited[ny][nx] == 1:
                                continue
                            visited[ny][nx] = 1
                            dists[ny][nx] = dists[_y][_x] + 1
                            q.append((ny,nx))
            print(dists)

            