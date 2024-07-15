# 가족인가? ( #1717 )
# https://www.acmicpc.net/problem/1717
# N과 M이 주어집니다. N은 집합의 개수이고, M은 연산의 개수입니다.
# 연산이 0 A B 의 형태로 주어졌을 때는 A가 B의 부모가 됩니다.
# 연산이 1 A B 의 형태로 주어졌을 때는 같은 족보인지 확인합니다.
# 1 A B 연산의 결과 같다면 YES를 다르다면 NO를 출력하세요.

# 입력
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1

# 출력
# NO
# NO
# YES



N, M = 7, 8 #map(int, input().split()) # N 집합의 갯수, M 연산의 갯수
operations = [[0, 1, 3], [1, 1, 7], [0, 7, 6], [1, 7, 1], [0, 3, 7], [0, 4, 2], [0, 1, 1], [1, 1, 1]] # [list(map(int, input().split())) for _ in range(M)]

parents = [i for i in range(N+1)] # [0, 1, 2, 3, 4, 5, 6, 7]

def _union(A, B):
    parents[B] = A # 부모를 바꾸어준다.

def _find(A):
    # root 조상이 나올 때까지 재귀 (부모가 없는 조상까지..)
    if parents[A] == A:
        return A
    else:
        return _find(parents[A])

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

