# 문제 4. RGB 색칠하기 ( #1149 )
# https://www.acmicpc.net/problem/1149
# 디자이너 정우는 한 거리의 건물들의 색을 바꾸려고 한다.
# Red, Green, Blue 세가지 색중에 하나를 선택해서 색을 바꾸려고 하는데
# 연속된 색으로 두 건물을 칠하면 건물들의 경계가 모호해져서 아름답지 않다.
# 건물의 개수 N과 건물을 R,G,B 로 색칠하는 비용이 주어졌을 때,
# 모든 집을 칠하는 비용의 최솟값을 구하는 프로그램을 작성하세요.

# 3
# 26 40 83
# 49 60 57
# 13 89 99
# 96

N = 3 # int(input())
# costs = [[26, 40, 83], [49, 60, 57], [13, 89, 99]] # [list(map(int, input().split())) for _ in range(N)]
costs = [[1, 100, 100], [100, 1, 100], [100, 100, 1]] # [list(map(int, input().split())) for _ in range(N)]

dp = [[-1 for _ in range(3)] for _ in range(N)]

dp[0] = costs[0]

for idx in range(1, N):
    for color in range(3): # R:0, G:1, B:2
        if color == 0: # RED
            dp[idx][color] = min(dp[idx-1][1], dp[idx-1][2]) + costs[idx][color]
        if color == 1: # GREEN
            dp[idx][color] = min(dp[idx-1][0], dp[idx-1][2]) + costs[idx][color]
        if color == 2: # BLUE
            dp[idx][color] = min(dp[idx-1][0], dp[idx-1][1]) + costs[idx][color]

print(min(dp[N-1]))