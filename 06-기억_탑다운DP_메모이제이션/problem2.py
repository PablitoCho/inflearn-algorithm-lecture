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

# 2차원 dp 테이블 [idx][weight]
dp = [[-1 for _ in range(100_001)] for _ in range(N)]

def recur(idx, weight):
    global ans
    if idx == N:
        return 0
    if weight > W:
        return -999999
    
    if dp[idx][weight] != -1:
        return dp[idx][weight]
    
    # 물건을 넣은 경우 vs 안 넣은 경우
    w, v = packages[idx]
    dp[idx][weight] = max(recur(idx+1, weight+w) + v, recur(idx+1, weight))
    return dp[idx][weight]

ans = recur(0, 0)
print(ans)

