# https://www.acmicpc.net/problem/2178
# 미로탐색 (최소한의 칸 수)
from collections import deque

# N : rows, M : cols
N, M = map(int, input().split())
# MAP = [[0] * M for _ in range(N)]
MAP = [list(map(int, list(input()))) for _ in range(N)]
print(MAP)
visited = [[False] * M for _ in range(N)]

moves = [[1,0], [-1,0], [0,1], [0,-1]]

def BFS(row, col):
    q = deque()
    q.append((row, col))
    visited[row][col] = True
    while q:
        current_row, current_col = q.popleft()
        for move in moves:
            dx, dy = move
            next_row, next_col = current_row + dx, current_col + dy
            if 0 <= next_row < N and 0 <= next_col < M:
                if MAP[next_row][next_col] == 1 and not visited[next_row][next_col]:
                    visited[next_row][next_col] = True
                    q.append((next_row, next_col))
                    MAP[next_row][next_col] = MAP[current_row][current_col] + 1

BFS(0, 0)

print(MAP[N-1][M-1])
