# https://www.acmicpc.net/problem/1463

# % 3, % 2, -1 중 하나의 연산을 사용하여 1로 만들기

N = int(input())
D = [-1 for _ in range(N+1)]

D[1] = 0
D[2] = 1
# bottom up DP
for i in range(3, N+1):
    D[i] = D[i-1] + 1 # -1
    if i % 2 == 0: # /2
        D[i] = min(D[i//2] + 1, D[i])
    if i % 3 == 0: # /3
        D[i] = min(D[i//3] + 1, D[i])

print(D[N])