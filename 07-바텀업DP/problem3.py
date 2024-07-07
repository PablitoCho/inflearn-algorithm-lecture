# 문제 3. 피보나치 타일링 ( #11726 )
# https://www.acmicpc.net/problem/11726
# 2xN 크기의 직사각형이 있습니다.
# 1x2, 2x1 크기의 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

# DP 문제 유형 (1) 완전탐색적, 추론이 가능한 DP, (2) 아이큐 테스트스러운 DP. 손으로 써보면서 규칙을 찾아내야 한다.

# 피보나치 수열.. 0, 1, 1, 2, 3, 5, 8, 13, ...
# dp[i] = dp[i-1]+dp[i-2]
import sys
sys.setrecursionlimit(10**6)
N = int(input())

dp = [-1 for _ in range(N+1)]

dp[0] = 1
dp[1] = 1

def fun(n):
    if dp[n] > -1:
        return dp[n]
    else:
        dp[n] = fun(n-1) + fun(n-2)
        return dp[n]

print(fun(N) % 10_007)