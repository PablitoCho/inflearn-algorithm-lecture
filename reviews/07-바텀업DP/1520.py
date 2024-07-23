# https://www.acmicpc.net/problem/1520

M, N = map(int, input().split())
coords = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]

# 모든 점을 방문한다!
# 방문시 이동할 수 있는 모든 경우의 수를 재귀로 구현!
# 재귀로 구현한 뒤 DP로 바꾼다!

# answer = 0
def solve(y, x):
    global answer
    if y == M-1 and x == N-1:
        return 1 # 도착지에 도달하면 +1. 도착하면 1을 갖고 돌아온다.
    
    if dp[y][x] >= 0: # 이미 DP 테이블에 업데이트된 경로라면 바로 return
        return dp[y][x]
    
    route = 0
    for dy, dx in [[1,0], [-1,0], [0,1], [0,-1]]:
        ny = y + dy
        nx = x + dx
        if (0 <= ny < M) and (0 <= nx < N):
            if coords[ny][nx] < coords[y][x]:
                # print(f"({x}, {y}) > ({nx}, {ny})")
                route += solve(ny, nx) # 갈 수 있는 모든 경로의 합
    dp[y][x] = route
    return route

answer = solve(0, 0)
print(answer)
print(dp)