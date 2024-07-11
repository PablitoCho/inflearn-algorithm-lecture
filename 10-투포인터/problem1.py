# 1. 두 수의 합( #3273 )
# https://www.acmicpc.net/problem/3273
# n개의 서로 다른 양의 정수로 이루어진 수열이 있습니다.
# 숫자의 범위는 1 ~ 1,000,000 입니다.
# 자연수 x가 주어집니다.
# 제공된 수열에서 두 수를 합해서 x가 나오는 모든 결과의 경우의 수를 구하세요.

# 입력
# 9
# 5 12 7 10 9 1 2 3 11
# 13

# 출력
# 3

N = 9 #int(input())
arr = [5, 12, 7, 10, 9, 1, 2, 3, 11] #list(map(int, input().split()))
value = 13 #int(input())

# 정렬
arr = sorted(arr) # [1, 2, 3, 5, 7, 9, 10, 11, 12]

# 두 개의 포인터 정의
x1 = 0
x2 = N-1

cnt = 0

while x1 < x2: # 투 포인터 x1과 x2가 서로 만나면 멈춰라.
    current = arr[x1] + arr[x2]
    if current == value:
        cnt += 1
    if current >= value:
        x2 -= 1
    if current < value:
        x1 += 1

print(cnt)
