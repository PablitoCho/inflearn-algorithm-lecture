# 문제 1. 상담 ( #14501 )
# https://www.acmicpc.net/problem/14501
# 상담원 정우는 곧 퇴사를 하려고 합니다.
# 퇴사 날은 N+1일 이라서, 남은 N일 동안 상담을 해서 돈을 많이 벌어서 나가고 싶습니다.
# 가장 돈을 많이 받도록 상담을 골라서 신청했을 때, 그 금액을 출력하는 프로그램을 작성하세요.


N = 7 #int(input())
schedules = [[4, 10], [1,20], [3,30],[1,40],[2,35],[3,150],[2,10]] #[list(map(int, input().split())) for _ in range(N)]

# 뒤에서부터 상담을 받거나 안 받거나.. 중에 더 좋은 것
dp = [-1 for _ in range(N+1)]


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

recur(0)

print(dp)