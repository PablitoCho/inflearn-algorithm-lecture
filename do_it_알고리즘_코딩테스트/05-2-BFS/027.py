# https://www.acmicpc.net/problem/2178
# 미로탐색 (최소한의 칸 수)
from collections import deque

N, M = map(int, input().split())
mat = [['0'] + list(input()) for _ in range(N)]
mat = [['0'] * (M+1)] + mat
visited = [[False for _ in range(M+1)] for _ in range(N+1)]
# print(mat)

q = deque()
q.append((1,1))
visited[1][1] = True

steps = 1

while q:
    x, y = q.popleft()
    if x == N and y == M: # DONE!
        break
    for move in [[1,0],[-1,0],[0,1],[0,-1]]:
        dx, dy = move
        nx = x + dx
        ny = y + dy
        if (1 <= nx < N+1) and (1 <= ny < M+1):
            if not visited[nx][ny]:
                if mat[nx][ny] == '1':
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    steps += 1

print(steps)