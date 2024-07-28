N = int(input())
D = [-1] * (N+1)

D[0] = 0
D[1] = 1

def fibo(n):
    if D[n] > -1:
        return D[n]
    D[n] = fibo(n-1) + fibo(n-2)
    return D[n]

answer = fibo(N)
print(answer)
