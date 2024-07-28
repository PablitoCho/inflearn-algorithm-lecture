# https://www.acmicpc.net/problem/1253

N = int(input())
arr = list(map(int, input().split()))
# print(arr)
# arr = sorted(arr)
arr.sort()

answer = 0

for k in range( N):
    number = arr[k]
    s = 0
    e = N - 1
    while s < e:
        total = arr[s] + arr[e]
        if total == number:
            answer += 1
            break
        elif total < number:
            s += 1
        else:
            e -= 1
        
print(answer)