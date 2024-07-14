# 트리 부모 찾기 ( #11725 )
# 노드의 개수 N이 주어집니다. 연결된 두 정점이 주어집니다.
# 루트가 1이라고 가정했을 때, 1을 제외한 노드들의 부모를 출력하세요.

# 입력 (부모, 자식 관계가 주어지지 않는다.)
# 7
# 1 6
# 6 3
# 3 5
# 4 1
# 2 4
# 4 7

# 출력
# 4
# 6
# 1
# 3
# 1
# 4

N = 7#int(input())
links = [[1, 6], [6, 3], [3, 5], [4, 1], [2, 4], [4, 7]]#[list(map(int, input().split())) for _ in range(N-1)]
graph = [[] for _ in range(N+1)]
children = [0 for _ in range(N+1)] # 자식의 갯수를 구하고 싶다면?

for link in links:
    a, b = link
    graph[a].append(b)
    graph[b].append(a)

print(graph)

# DFS
def recur(node, prev):
    for nxt in graph[node]:
        if nxt == prev:
            continue # 역주행 방지
        recur(nxt, node)
    # 자식의 정보를 부모로 넘기기 위해서는 후위순회 필요
    children[prev] += 1

recur(1, 0)
print(children) # [1, 2, 0, 1, 2, 0, 1, 0]