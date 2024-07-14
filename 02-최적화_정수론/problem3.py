# 문제 3. 숨어 있는 숫자 찾기 ( #1407, # 2247 )
# https://www.acmicpc.net/problem/1407
# 15 = 2^0 * 2 * 5 = f(15) = 1
# 40 = 2^3 * 5 => f(40) = 8
# given A, B... A<=B .. f(A) + f(A+1) + ... + f(B-1) + f(B)

A, B = map(int, input().split())
def cal(number):
    divisor = 1
    while number % divisor == 0:
        divisor *= 2
    return int(divisor / 2)

answer = 0
for x in range(A, B+1):
    answer += cal(x)
print(answer)