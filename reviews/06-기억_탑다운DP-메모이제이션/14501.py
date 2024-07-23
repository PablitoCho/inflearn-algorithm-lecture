# https://www.acmicpc.net/problem/14501

N = int(input())
pairs = [list(map(int, input().split())) for _ in range(N)]

# 내 답안
# answer = 0
# def solve(day, revenue):
#     global answer
#     if day > N-1:
#         answer = max(answer, revenue)
#         return
    
#     d, r = pairs[day]
#     if day + d > N:
#         solve(day + 1, revenue)
#         return
#     # take
#     solve(day + d, revenue + r)
#     # not take
#     solve(day + 1, revenue)
# solve(0, 0) # 첫 스케줄 첫날부터 수입 0원
# print(answer)

# DP 사용
dp = [-1 for _ in range(N+1)] # 퇴사날(N+1일)까지 상담을 받거나 안 받거나 중에 더 좋은 것..
# 특정일에 상담을 받거나 안 받거나.. 그 중에 더 수익이 높은 경우를 저장
def recur(idx):
    global dp
    if idx == N-1: # 퇴사날에 딱 맞춰 도착
        return 0
    if idx > N-1:
        return -999999999
    if dp[idx] > -1:
        return dp[idx]
    d, r = pairs[idx]
    # 상담을 하거나 안 하거나 중 더 수익이 높은 경우를 dp에 저장
    dp[idx] = max(recur(idx + d) + r, recur(idx + 1))
    return dp[idx]

recur(0)
print(dp)

