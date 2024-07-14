# 보물섬( #2589 )
# https://www.acmicpc.net/problem/2589
# 바다와 섬을 아래와 같이 스트링으로 표현했습니다.
# 바다라면 Water의 W를 섬이라면 Land의 L로 표시했습니다.
# 섬에서 한 점과 한 점의 위치가 가장 먼곳에 보물이 숨겨져 있습니다.
# 보물사이의 최단 거리를 구하세요.

# 입력
# 5 7
# WLLWWWL
# LLLWLLL
# LWLWLWW
# LWLWLLL
# WLLWLWW

# 출력
# 8

# 이런 상황의 그래프 탐색은 BFS가 좋다...! (DFS로는 최단 거리를 보장해서 탐색할 수가 없다)
from collections import deque

# Y, X = map(int, input().split())
# graph = [list(input().rstrip()) for _ in range(Y)]
Y, X = 5, 7
graph = [['W', 'L', 'L', 'W', 'W', 'W', 'L'], ['L', 'L', 'L', 'W', 'L', 'L', 'L'], ['L', 'W', 'L', 'W', 'L', 'W', 'W'], ['L', 'W', 'L', 'W', 'L', 'L', 'L'], ['W', 'L', 'L', 'W', 'L', 'W', 'W']]

# print(graph)

maxi = 0

for y in range(Y):
    for x in range(X):
        if graph[y][x] == 'L':
            visited = [[0 for _ in range(X)] for _ in range(Y)]
            dist = [[0 for _ in range(X)] for _ in range(Y)]
            # BFS
            q = deque()
            q.append([y,x]) # 시작점
            visited[y][x] = 1 # 시작점 방문처리
            while q:
                ey, ex = q.popleft()
                # 4방향 탐색
                for dy, dx in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    ny, nx = ey + dy, ex + dx
                    if 0 <= ny < Y and 0 <= nx < X:
                        if graph[ny][nx] == 'L': # 땅이라면?
                            if visited[ny][nx] == 0: # 방문한 적이 없다면?
                                visited[ny][nx] = 1
                                dist[ny][nx] = dist[ey][ex]+1
                                maxi = max(maxi, dist[ny][nx])
                                q.append([ny,nx])

print(maxi)