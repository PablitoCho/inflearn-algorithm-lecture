# https://www.acmicpc.net/problem/2805
N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    woods = sum(map(lambda x: max(0, x-mid), trees))
    if woods > M: # 낮추자
        start = mid + 1
    elif woods < M: # 높히자
        end = mid - 1
    else:
        break
    
print(mid)