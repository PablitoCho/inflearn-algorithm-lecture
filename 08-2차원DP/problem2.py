# 문제 2. 끝까지 이동하기 ( #1520 )
# https://www.acmicpc.net/problem/1520
# 좌측 위 좌표에서 출발합니다.
# 아래와 같은 조건이 주어졌을 때, 우측 하단까지 도달 할 수 있는 경로의 수를 구하세요.

# [조건]
# -	이동은 반드시, 현재 좌표의 값보다 더 작은 곳으로만 이동이 가능합니다.

# 입력
# 4 5
# 50 45 37 32 30
# 35 50 40 20 25
# 30 30 25 17 28
# 27 24 22 15 10
# 출력
# 3

Y, X = 4, 5 #map(int, input().split())
#[list(map(int, input().split())) for _ in range(Y)]
graph = [[50, 45, 37, 32, 30], [35, 50, 40, 20, 25], [30, 30, 25, 17, 28], [27, 24, 22, 15, 10]]

dp = [[-1 for _ in range(X)] for _ in range(Y)]

# print(graph)
def recur(y, x):
    if x == X-1 and y == Y-1:
        return 1

    if dp[y][x] >= 0:
        return dp[y][x]
    current = graph[y][x]

    route = 0
    for dy, dx in [[1,0], [-1,0],[0,1],[0,-1]]:
        _y = y+dy
        _x = x+dx
        if 0 <= _y < Y and 0 <= _x < X:
            if current > graph[_y][_x]:
                route += recur(_y, _x)

    dp[y][x] = route  
    return dp[y][x]

print(recur(0, 0))
print(dp)