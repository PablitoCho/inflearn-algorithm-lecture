#https://www.acmicpc.net/problem/2018
N = int(input())

s = 1
e = 1
total = 1
answer = 1
while e < N:
    # total = sum([i for i in range(s, e+1)])
    if total == N:
        answer += 1
        e += 1
        total += e
    elif total > N:
        total -= s
        s += 1
    else: # total < N
        e += 1
        total += e

print(answer)