# LCS (Longest Common Subsequence)
# 점화식
# 1) LCS(0, 0) = 0
# 2) x[i] == y[j] ? LCS(i, j) = LCS(i-1, j-1) + 1
# 3) x[i] != y[j] ? LCS(i, j) = max(LCS(i-1, j), LCS(i, j-1))

str1 = "ABDFEGACB"
str2 = "BXDEGK"

dp = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        char1 = str1[i-1]
        char2 = str2[j-1]
        if char1 == char2:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(str1)][len(str2)])