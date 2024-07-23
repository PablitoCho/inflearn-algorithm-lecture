# MST ( 최소 스패닝 트리 ) 1197
# https://www.acmicpc.net/problem/1197
# 노드의 개수 N과 링크의 개수 M이 주어집니다.
# M개 만큼 연결되어 있는 노드 A,B와 가중치 C가 주어집니다.
# 모든 노드를 최소 비용(가중치의 합)으로 연결했을 때의 비용을 계산하세요.

# 입력
# 3 3
# 1 2 1
# 2 3 2
# 1 3 3

# 출력
# 3

# 주어진 그래프를 트리로 바꾼다. (싸이클을 끊는다.)
# 단, 되도록 가중치가 높은 링크를 지워 최소의 비용으로 뻗어나가는 트리를 만들어야 한다.

# 크루스칼
# 먼저 모든 링크들의 정보를 다 가져온다. 유니온/파인드 -> 같은 집합인지(연결되어 있는지)확인 가능
# [1,2,4,5,7]

N, M = 3, 3 #map(int, input().split())

def _find(x):
    while parents[x] != x: # root가 아니면 반복
        x  = parents[x]
    return x # 연결되어 있는 가장 꼭대기 root 출력

def _union(a, b):
    # 부모끼리 붙인다
    a = _find(a)
    b = _find(b)
    if a == b:
        return # 같은 집합이면 무시
    elif ranks[a] < ranks[b]:
        parents[a] = b
    elif ranks[a] > ranks[b]:
        parents[b] = a
    else: # ranks[a] == ranks[b] 어느 쪽으로 연결되어도 상관없다
        parents[a] = b
        ranks[b] += 1

# 크루스칼
# 1. 모든 링크를 한 번에 가져온다
links = [[1, 2, 1], [2, 3, 2], [1, 3, 3]] #[list(map(int, input().split())) for _ in range(M)]
links.sort(key = lambda x:x[2]) # 가중치(3번째 값) 기준으로 정렬
# 2. 링크를 연결하면서 같은 집합으로 만들어준다
parents = [i for i in range(1_000_001)]
ranks = [0 for _ in range(1_000_001)]
# 3. 만약에 이미 같은 집합이라면 연결하지 않는다
answer = 0
for link in links:
    a, b, w = link

    a = _find(a)
    b = _find(b)
    if a == b:
        # 연결되어있다. 넘어간다
        continue
    else: # 연결한다.
        _union(a,b)
        answer += w

print(answer)
