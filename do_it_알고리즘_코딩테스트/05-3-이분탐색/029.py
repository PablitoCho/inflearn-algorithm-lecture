# https://www.acmicpc.net/problem/1920

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

M = int(input())
tries = list(map(int, input().split()))

# print(arr, tries)
def search(n):
    start = 0
    end = N-1
    while start <= end:
        mid = (start + end) // 2
        # print(f'given {n} current {arr[mid]}')
        if arr[mid] == n:
            return 1
        if arr[mid] > n:
            end = mid - 1
        else: # arr[mid] < n
            start = mid + 1
    return 0

for n in tries:
    print(search(n))