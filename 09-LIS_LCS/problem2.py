# 두 수열에 포함되는 가장 긴 부분 문자열 ( #9251 )
# https://www.acmicpc.net/problem/9251
# 두 문자열이 주어집니다.
# 양 쪽 문자열에 공통적으로 포함되는 가장 긴 부분 문자열의 길이를 계산하시오.

# 입력
# ACAYKP
# CAPCAK

# 출력
# 4
# why ? ACAK
arr1 = "ACAYKP" #input()
arr2 = "CAPCAK" #input()

# 끝의 문자가 같다면
# LCS(M,N) = LCS(M-1, N-1) + 1
# 다르다면
# LCS(M,N) = max(LCS(M-1,N), LCS(M,N-1))

dp = [[0 for _ in range(len(arr2)+1)] for _ in range(len(arr1)+1)]

for i in range(1, len(arr1)+1):
    for j in range(1, len(arr2)+1):
        if arr1[i-1] == arr2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(arr1)][len(arr2)])