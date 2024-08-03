# https://www.acmicpc.net/problem/1753
V, E = 5, 6 #map(int, input().split())
start = 1 #int(input())
edges = [[5, 1, 1], [1, 2, 2], [1, 3, 3], [2, 3, 4], [2, 4, 5], [3, 4, 6]] #[list(map(int, input().split())) for _ in range(E)]
graph = [[] for _ in range(V+1)]
for edge in edges:
    s, e, w = edge
    graph[s].append((e, w))
# print(edges)
distances = [float("inf") for _ in range(V+1)]


import heapq
q = []
distances[start] = 0
heapq.heappush(q, (0, start))

while q:
    current_weight, current_node = heapq.heappop(q)
    if distances[current_node] < current_weight:
        continue
    for nxt_node, nxt_weight in graph[current_node]:
        distances[nxt_node] = min(distances[current_node] + nxt_weight, distances[nxt_node])
        heapq.heappush(q, (distances[nxt_node], nxt_node))

print(distances)