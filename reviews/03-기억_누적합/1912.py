# https://www.acmicpc.net/problem/1912
# 입력 출력
# 10
# 10 -4 3 1 5 6 -35 12 21 -1
# 33

# 10
# 2 1 -4 3 4 -4 6 5 -5 1
# 14

N = 10 #int(input())
arr =[10, -4, 3, 1, 5, 6, -35, 12, 21, -1] #list(map(int, input().split()))

cumulative_sum = [0 for _ in range(N+1)]

for i in range(N):
    cumulative_sum[i+1] = max(cumulative_sum[i] + arr[i], arr[i])
print(cumulative_sum)
