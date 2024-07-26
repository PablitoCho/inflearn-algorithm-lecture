# https://www.acmicpc.net/problem/3273

N = int(input())
arr = list(map(int, input().split()))
X = int(input())

# 정렬이 필요하다
arr = sorted(arr)
x1 = 0
x2 = N-1

answer = 0
while x1 < x2:
    current = arr[x1] + arr[x2]
    if current == X:
        answer += 1
    if current < X:
        x1 += 1
    if current >= X:
        x2 -= 1

print(answer)