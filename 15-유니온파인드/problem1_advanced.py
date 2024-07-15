# 가족인가? ( #1717 )
# https://www.acmicpc.net/problem/1717

N, M = 7, 8 #map(int, input().split()) # N 집합의 갯수, M 연산의 갯수
operations = [[0, 1, 3], [1, 1, 7], [0, 7, 6], [1, 7, 1], [0, 3, 7], [0, 4, 2], [0, 1, 1], [1, 1, 1]] # [list(map(int, input().split())) for _ in range(M)]

parents = [i for i in range(N+1)] # [0, 1, 2, 3, 4, 5, 6, 7]
ranks = [0 for _ in range(N+1)]

def _union(A, B):
    # parents[B] = A # 부모를 바꾸어준다.
    A = _find(A)
    B = _find(B)
    # 최대 높이를 확인하여 rank를 고려하여 union한다.
    if A == B:
        return # 이미 같은 것들끼리는 합칠 필요없다
    if ranks[A] < ranks[B]: # 최대높이가 더 큰 것을 짧은 쪽에 붙인다.
        parents[B] = A
    elif ranks[A] > ranks[B]:
        parents[A] = B
    else:
        parents[A] = B # 반대로 해도 상관없음
        ranks[B] += 1

# 재귀 최적화 필요.. 최악의 트리가 나올 수도 있다.. 1억개가 한쪽 자식으로만 쭉 연결되어 있는..
def _find(A):
    # root 조상이 나올 때까지 재귀 (부모가 없는 조상까지..)
    if parents[A] == A:
        return A
    else:
        parents[A] = _find(parents[A]) # 경로 단축 최적화
        return parents[A]

for operation in operations:
    X, A, B = operation
    if X == 0:
        _union(A, B)
    if X == 1:
        if _find(A) == _find(B):
            # 같은 조상 (같은 족보, 같은 집합)
            print("YES")
        else:
            print("NO")

