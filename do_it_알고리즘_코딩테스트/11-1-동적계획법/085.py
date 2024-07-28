# https://www.acmicpc.net/problem/14501

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

D = [0] * (N+2) # D[i]? i날부터 퇴사일까지 벌 수 있는 최대 수익
# print(table)
# top down
# 점화식
# D[i] = D[i+1] (오늘 시작한 상담이 마지막날까지 끝나지 않는 경우)
# D[i] = max(D[i+1], D[i+Ti] + Pi) # 상담을 진행하지 않는 경우 (D[i+1]), 진행하지 않는 경우 D[i+Ti] + Pi

# D[7] = 0

for i in range(N, 0, -1):
    T, P = table[i-1]
    if i + T > N+1:
        D[i] = D[i+1]
    else:
        D[i] = max(D[i + T] + P, D[i])

print(D)