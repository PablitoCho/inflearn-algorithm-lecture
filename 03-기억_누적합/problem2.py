# 문제 2. 수열 가장 크게 만들기 ( #1912 )
# https://www.acmicpc.net/problem/1912
# 수열의 길이 N과 수열이 주어집니다.
# 연속된 몇 개의 수를 선택하여 구할 수 있는 합 중에서, 가장 큰 합을 구하는 프로그램을 작성하세요.

# 10
# 10 -4 3 1 5 6 -35 12 21 -1
# 33

# Dynamic Programming - Memoization

# N = int(input())
# arr = list(map(int, input().split()))

# partial_sum = [0 for _ in range(N+1)]
# for i in range(N):
#     partial_sum[i+1] = partial_sum[i] + arr[i]

# # sums = []
# answer = 0
# for k in reversed(range(1, N+1)):
#     for j in range(k):
#         # sums.append(partial_sum[k] - partial_sum[j])
#         answer = max(answer, partial_sum[k] - partial_sum[j])

# print(answer)

N = int(input())
arr = list(map(int, input().split()))

prefix = [0 for _ in range(N+1)]

for i in range(N):
    # 지금까지 더해온 합보다 현재 위치의 값이 더 크다면, 이전까지의 값을 무시하고 새로 시작. 그 이후의 값으로 넘길 이유가 없다.
    prefix[i+1] = max(prefix[i] + arr[i], arr[i])

print(max(prefix))