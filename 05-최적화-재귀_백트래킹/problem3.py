# 문제 3. 상담 ( #14501 )
# https://www.acmicpc.net/problem/14501
# 상담원 정우는 곧 퇴사를 하려고 합니다.
# 퇴사 날은 N+1일 이라서, 남은 N일 동안 상담을 해서 돈을 많이 벌어서 나가고 싶습니다.
# 가장 돈을 많이 받도록 상담을 골라서 신청했을 때, 그 금액을 출력하는 프로그램을 작성하세요.

# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200

N = 7 #int(input())
schedules = [[3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]] #[list(map(int, input().split())) for _ in range(N)]

answer = 0

def recur(idx, money):
    global answer
    if idx > N:
        return
    
    if idx == N:
        answer = max(answer, money)
        return
    
    days, pay = schedules[idx]
    # 상담 진행
    if idx+days < N:
        recur(idx+days, money+pay)
    # 상담 진행 X
    recur(idx+1, money)

recur(0, 0)

print(answer)


# 다이나믹 프로그래밍!
# 점화식을 세워라!
# dp[i] = dp[i-schedules[idx][0]]...