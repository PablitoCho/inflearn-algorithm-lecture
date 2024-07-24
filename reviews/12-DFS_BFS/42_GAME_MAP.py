# 게임 맵 최단거리 (416p)
# 게임 맵이 주어졌을 때, 우리팀 캐릭터가 상대 진영에 도달할 수 있는 최단거리를 반환하는 함수 solution을 완성하시오. 도달이 불가능한 경우 -1을 반환
# case 1
# maps [[1,0,1,1,1], [1,0,1,0,1], [1,0,1,1,1], [1,1,1,0,1], [0,0,0,0,1]]
# answer 11

# case 2
# maps [[1,0,1,1,1], [1,0,1,0,1], [1,0,1,1,1], [1,1,1,0,0], [0,0,0,0,1]]
# answer -1

maps = [[1,0,1,1,1], [1,0,1,0,1], [1,0,1,1,1], [1,1,1,0,0], [0,0,0,0,1]]
H = len(maps)
W = len(maps[0])
distances = [[-1] * W for _ in range(H)]

# maps[y][x]
from collections import deque

q = deque()

answer = -1
q.append((0, 0))
distances[0][0] = 1

while q:
    cy, cx = q.popleft() # current location (y, x)
    if cy == H-1 and cx == W-1:
        break
    for move in [[1,0], [-1,0], [0,1], [0,-1]]:
        ny, nx = cy + move[0], cx + move[1]
        if 0 <= ny < H and 0 <= nx < W and maps[ny][nx] == 1: # 이동 가능한 위치
            if distances[ny][nx] == -1: # 처음 방문했다면..
                q.append((ny, nx))
                distances[ny][nx] = distances[cy][cx] + 1

print(distances[H-1][W-1])
                
        

