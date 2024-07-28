# https://www.acmicpc.net/problem/1806
# 길이 N의 수열의 부분 수열의 합이 S 이상이 되는 가장 짧은 길이를 구하시오

N, S = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
summ = 0 # 업데이트하면서 유지한다.
answer = 100_001

while True:
    if summ >= S:
        answer = min(answer, right - left)
        summ -= arr[left]
        left += 1
    elif right == N:
        break
    else: #summ < S
        summ += arr[right]
        right += 1

if answer == 100_001:
    print(0)
else:
    print(answer)

