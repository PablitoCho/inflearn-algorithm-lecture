# https://www.acmicpc.net/problem/16472
N = int(input()) # 인식할 수 있는 알파벳의 종류 (1 < N <= 26)
arr = input().rstrip() #list(map(int, input().split()))

start = 0
end = 0

dict = {}

answer = 0

for end in range(len(arr)):
    dict.setdefault(arr[end], 0)
    dict[arr[end]] += 1
    while len(dict) > N:
        dict[arr[start]] -= 1
        if dict[arr[start]] == 0:
            del dict[arr[start]]
        start += 1
    answer = max(answer, end - start + 1)

print(answer)
