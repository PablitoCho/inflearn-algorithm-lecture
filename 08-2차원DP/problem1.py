# 문제 1. 많이 이동하기 ( #1937 )
# https://www.acmicpc.net/problem/1937
# 모든 좌표에서 출발이 가능합니다.
# 아래와 같은 조건이 주어졌을 때, 가장 많이 이동한 경우 몇 회 이동했는지 계산하는 프로그램을 작성하세요.

# [조건]
# -	이동은 반드시, 현재 좌표의 값보다 더 큰 곳으로만 이동이 가능합니다.

# 입력
# 4
# 14 9 12 10
# 1 11 5 4
# 7 15 2 13
# 6 3 16 8
# 출력
# 4 

N = 4 # int(input())
graph = [[14, 9, 12, 10], [1, 11, 5, 4], [7, 15, 2, 13], [6, 3, 16, 8]] #[list(map(int, input().split())) for _ in range(N)]

## 총 세가지 스텝
# 모든 점을 방문한다
# def recur(y, x):
#     point = 0
#     current_value = graph[y][x]
#     for dy, dx in [[1,0], [-1,0], [0,1], [0,-1]]: # 상,하,좌,우
#         _y = y+dy
#         _x = x+dx
#         if 0 <= _y < N and 0 <= _x < N :
#             if current_value < graph[_y][_x]:
#                 point = max(recur(_y, _x) + 1, point)
#     return point

# for y in range(N):
#     for x in range(N):
#         print(f"{y}, {x} = {recur(y, x)}")

# 방문한 뒤에 이동할 수 있는 모든 경우의 수를 재귀로 구현한다

# 재귀로 구현한 뒤 DP로 바꾼다
dp = [[0 for _ in range(N)] for _ in range(N)]

def recur(y, x):
    if dp[y][x] > 0:
        return dp[y][x]
    point = 0
    current_value = graph[y][x]
    for dy, dx in [[1,0], [-1,0], [0,1], [0,-1]]: # 상,하,좌,우
        _y = y+dy
        _x = x+dx
        if 0 <= _y < N and 0 <= _x < N :
            if current_value < graph[_y][_x]:
                point = max(recur(_y, _x) + 1, point)
    
    dp[y][x] = point
    return dp[y][x]

for y in range(N):
    for x in range(N):
        recur(y,x)
        # print(f"{y}, {x} = {recur(y, x)}")

# print(dp)
print(max(map(max, dp)) + 1)