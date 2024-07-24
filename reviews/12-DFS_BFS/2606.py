# https://www.acmicpc.net/problem/2606
# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

N = int(input()) # node 수
M = int(input()) # edge 수

edges = [list(map(int, input().split())) for _ in range(M)] # edges [[1, 2], [2, 3], [1, 5], [5, 2], [5, 6], [4, 7]]

graph = [[] for _ in range(N+1)] # [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
visited = [0 for _ in range(N+1)]
for edge in edges:
    from_node, to_node = edge
    graph[from_node].append(to_node)
    graph[to_node].append(from_node)

# BFS (while queue)
# from collections import deque
# q = deque()
# q.append(1) # 출발 위치

# while q:
#     node = q.popleft()
#     visited[node] = 1
#     for neighbor in graph[node]:
#         if visited[neighbor] == 1:
#             continue
#         q.append(neighbor)

# print(sum(visited)-1) # 1번 노드는 제외

# DFS (재귀)
def solve(node):
    if visited[node] == 1:
        return
    visited[node] = 1
    for neighbor in graph[node]:
        solve(neighbor)

solve(1)
print(sum(visited)-1)


