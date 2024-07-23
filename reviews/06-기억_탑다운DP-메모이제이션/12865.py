# https://www.acmicpc.net/problem/12865

N, K = map(int, input().split())
WVs = [list(map(int, input().split())) for _ in range(N)]

# 무게와 물건에 대한 2차원 dp 테이블
dp = [[-1 for _ in range(100_001)] for _ in range(N)] # dp[무게][물건] dp[12][3]

def recur(idx, weight):
    if idx == N:
        return 0
    if weight > K:
        return -9999999
    if dp[idx][weight] > -1:
        return dp[idx][weight]
    w, v = WVs[idx]
    dp[idx][weight] = max(recur(idx+1, weight+w) + v, recur(idx+1, weight))
    return dp[idx][weight]
    
recur(0, 0)
print(max())

