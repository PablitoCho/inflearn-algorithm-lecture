# https://www.acmicpc.net/problem/1937

N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]
# [[14, 9, 12, 10],
#  [1, 11, 5,  4],
#  [7, 15, 2,  13], 
#  [6, 3,  16, 8]]

# 경우의 수(재귀식으로 순회) -> DP에 저장 -> 점화식으로 시작

# 모든 점을 방문한다!
# 방문시 이동할 수 있는 모든 경우의 수를 재귀로 구현!
# 재귀로 구현한 뒤 DP로 바꾼다!

dp = [[0 for _ in range(N)] for _ in range(N)]
def solve(y, x):
    if dp[y][x] > 0:
        return dp[y][x]
    for dy, dx in [[1,0], [-1,0], [0,1], [0,-1]]: # 이 네가지 경우 중 가장 큰 값을 가져오는 경우를 return
        ny = y + dy
        nx = x + dx
        if (0 <= nx < N) and (0 <= ny < N):
            if forest[y][x] < forest[ny][nx]:
                # 이동을 하고 돌아오면 + 1
                dp[y][x] = max(solve(ny, nx) + 1, dp[y][x])
    return dp[y][x]

for y in range(N):
    for x in range(N):
        solve(y, x)
# [0, 2, 0, 1], 
# [2, 1, 2, 3], 
# [1, 0, 3, 0], 
# [2, 3, 0, 1]
print(dp)