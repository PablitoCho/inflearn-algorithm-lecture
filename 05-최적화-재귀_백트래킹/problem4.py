# 문제 4. 냅색 ( #12865 )
# https://www.acmicpc.net/problem/12865
# 물건의 수 A와 배낭의 무게 B가 주어집니다.
# 순서대로 물건의 무게 W와 가치 V가 주어집니다.
# 배낭에 가장 가치있게 담았을 경우의 가치를 출력하는 프로그램을 작성하세요.

# 4 7 물품의 수, 버틸 수 있는 무게
# 6 13 물건의 무게와 가치...
# 4 8
# 3 6
# 5 12
# 14 # 배낭에 담을 수 있는 물건들의 가치 합의 최대값

# 완전 탐색적으로 생각하기...
N, W = 4, 7 #map(int, input().split())
packages = [[6, 13], [4, 8], [3, 6], [5, 12]] #[list(map(int, input().split())) for _ in range(N)]

answer = 0

def recur(idx, weight, value):
    global answer
    if idx == N:
        answer = max(answer, value)
        return
    w, v = packages[idx]
    # 담거나
    if weight + w <= W:
        recur(idx+1, weight+w, value+v)
    # 안 담거나
    recur(idx+1, weight, value)

recur(0, 0, 0)
print(answer)
