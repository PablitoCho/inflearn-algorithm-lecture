# 문제 1. 상담 ( #14501 )
# https://www.acmicpc.net/problem/14501

N = 7 #int(input())
schedules = [[4, 10], [1,20], [3,30],[1,40],[2,35],[3,150],[2,10]] #[list(map(int, input().split())) for _ in range(N)]


def recur(idx):
    if idx == N-1:
        return 0
    if idx > N-1:
        return -999999999
    
    if dp[idx] != -1:
        return dp[idx]

    d, p = schedules[idx]
    # 상담을 하는 경우 vs 안 하는 경우 중 큰 값을 dp[idx]에 저장(기억)하겠다.
    dp[idx] = max(recur(idx+d) + p, recur(idx+1))
    return dp[idx]


# 뒤에서부터 상담을 받거나 안 받거나.. 중에 더 좋은 것
dp = [0 for _ in range(N+1)]

#탑다운 DP. 더 강해지고 완벽해진 반복문
for idx in reversed(range(N)):
    if idx + schedules[idx][0] > N :
        dp[idx] = dp[idx+1] # 범위를 벗어난다면 해당 일의 상담은 선택하지 않는다
    else:
        dp[idx] = dp[idx] = max(dp[idx + schedules[idx][0]] + schedules[idx][1], dp[idx+1])
    
print(dp)

