# 문제 1. 수열 ( #2559 )
# https://www.acmicpc.net/problem/2559
# 수열의 길이 A와, 간격 B가 주어집니다.
# 그리고 수열이 하나 주어집니다.
# 주어진 간격만큼의 합을 구해서, 가장 큰 수를 출력하는 프로그램을 작성하세요.

# 10 2
# 3 -2 -4 -9 0 3 7 13 8 -3
# 21

# n, d = map(int, input().split())
# seq = list(map(int, input().split()))
# max = 0

# for i in range(n-(d-1)):
#     s = sum(seq[i:i+d])
#     if s >= max:
#         max = s

# print(max)

# 누적합을 사용하면 연산속도가 엄청 빨라진다. = 컴퓨터에게 기억하는 방법을 가르친다 (컴퓨터 연산의 한계를 극복하기 위해..)
A, B = map(int, input().split()) # A : 수열의 크기, B : 부분 합의 간격
arr = list(map(int, input().split()))

prefix = [0 for _ in range(A+1)] # 한 칸 더 크게 만든다.. 

for i in range(A):
    prefix[i+1] = prefix[i] + arr[i]

answer = []
for k in range(B, A+1):
    answer.append(prefix[k] - prefix[k-B])
print(max(answer))