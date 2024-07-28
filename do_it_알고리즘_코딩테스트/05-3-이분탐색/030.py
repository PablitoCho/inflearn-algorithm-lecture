# https://www.acmicpc.net/problem/2343
# 가능한 블루레이 크기 중 최소를 출력하시오

N, M = map(int, input().split()) # 강의 수, 블루레이 수
lectures = list(map(int, input().split()))
# print(lectures)

start = max(lectures)
end = sum(lectures)
# print(start, end)

while start <= end:
    mid = (start + end) // 2
    total = 0
    count = 0
    # mid로 모든 레슨이 저장 가능한가?
    for i in range(N):
        if total + lectures[i] > mid:
            count += 1
            total = 0
        total += lectures[i]
    if total != 0:
        count += 1
    if count > M:
        start = mid + 1
    else: # count < M
        end = mid - 1

print(start)