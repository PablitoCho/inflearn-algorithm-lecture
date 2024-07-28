# https://www.acmicpc.net/problem/1450
# 냅색 문제
# N 물건 수 < 30
# C 최대 무게 < 10^9
# 가방에 넣을 방법의 수
N, C = map(int, input().split())
weights = list(map(int, input().split()))
assert N == len(weights)
weights.sort()

dp = [[0 for _ in range(C)] for _ in range(N)] # dp[가방][무게]


...