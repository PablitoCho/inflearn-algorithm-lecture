# https://www.acmicpc.net/problem/1940
N = int(input())
M = int(input())
numbers = list(map(int, input().split()))

numbers = sorted(numbers)

start = 0
end = N-1

answer = 0
while start < end:
    hap = numbers[start] + numbers[end]
    if hap == M:
        answer += 1
        start += 1
        end -= 1
    elif hap > M:
        end -= 1
    else: # hap < M
        start += 1

print(answer)