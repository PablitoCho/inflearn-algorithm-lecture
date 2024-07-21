# https://www.acmicpc.net/problem/2559
# 입력, 출력
# 10 2
# 3 -2 -4 -9 0 3 7 13 8 -3
# 21

# 10 5
# 3 -2 -4 -9 0 3 7 13 8 -3
# 31

# N 날짜의 수, K 연속되는 일 수
N, K = 10, 5 #map(int, input().split())
arr = [3, -2, -4, -9, 0, 3, 7, 13, 8, -3] #list(map(int, input().split()))

cumulative_sum = [0 for _ in range(N+1)]

for i in range(N):
    cumulative_sum[i+1] = cumulative_sum[i] + arr[i]

answer = 0
for j in range(K, N+1):
    temp = cumulative_sum[j] - cumulative_sum[j-K]
    answer = max(answer, temp)

print(answer)
