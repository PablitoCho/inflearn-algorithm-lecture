# 깊이 우선 탐색으로 모든 그래프의 노드를 순회하는 함수 solution을 완성하시오

# 1
# graph [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']]
# start 'A'
# return ['A', 'B', 'C', 'D', 'E']

# 2
# graph [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']]
# start 'A'
# return ['A', 'B', 'D', 'E', 'F', 'C']

graph = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']]
start = 'A'

edges = {}
for g in graph:
    node1, node2 = g
    if not node1 in edges:
        edges[node1] = []
    edges[node1].append(node2)
    if not node2 in edges:
        edges[node2] = []
    edges[node2].append(node1)
# print(edges)

visited = []

def solve(node):
    if node in visited:
        return
    visited.append(node)
    for neighbor in edges[node]:
        solve(neighbor)

solve(start)

print(visited)

# 시간 복잡도?
# 노드 N, 간선 E?
# 인접 리스트 생성시, 간선 갯수만큼 ..
# 각 노드를 1회씩 방문
# O(N+E)