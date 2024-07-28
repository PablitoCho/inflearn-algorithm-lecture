# https://www.acmicpc.net/problem/1717
N, M = map(int, input().split())
ops = [list(map(int, input().split())) for _ in range(M)]

parents = [i for i in range(N+1)]

def _union(A, B):
    parents[B] = A

def _find(A):
    if parents[A] == A:
        return A
    else:
        return _find(parents[A])

for op in ops:
    X, A, B = op
    if X == 0:
        _union(A, B)
    elif X == 1:
        if _find(A) == _find(B):
            print("YES")
        else:
            print("NO")
