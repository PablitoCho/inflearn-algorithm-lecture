# 문제 4. 냅색 ( #12865 )
# https://www.acmicpc.net/problem/12865

N, W = 4, 7 #map(int, input().split())
packages = [[6, 13], [4, 8], [3, 6], [5, 12]] #[list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(W+1) for _ in range(N+1)]

for n in range(N+1): # 물건
    for w in range(W+1): # 무게
        if w < W :
            dp[n][w] = dp[n-1][w]
        else:
            dp[n][w] = max(
                dp[n-1][w - packages[n][0]] + packages[n][1],
                dp[n-1][w]
            )

print(dp)
