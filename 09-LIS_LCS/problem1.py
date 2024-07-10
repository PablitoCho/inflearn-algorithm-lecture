# 가장 긴 증가하는 부분 수열 ( #11053, #2565 )
# https://www.acmicpc.net/problem/11053
# 수열이 주어집니다.
# 수열의 가장 긴 증가하는 부분 수열의 길이를 계산하시오.
# 입력
# 6
# 10 20 10 30 20 50
# 출력
# 4
# "10 20 30 50”

N = 6 # int(input())
arr = [10, 20, 10, 30, 20, 50] # list(map(int,input().split()))

dp = [1 for _ in range(N)]

for i in range(N): # 0 1 2 3 4 5
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
