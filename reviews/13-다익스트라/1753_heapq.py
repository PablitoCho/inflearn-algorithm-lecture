# https://www.acmicpc.net/problem/1753

V, E = map(int, input().split())
start = int(input())
edges = [list(map(int, input().split())) for _ in range(E)]

graph = [[] for _ in range(V+1)]
for edge in edges:
    x, y, w = edge
    graph[x].append((y,w))

import heapq
distances = [1e9 for _ in range(V+1)]
q = []
heapq.heappush(q, [0, start])
distances[start] = 0

while q:
    heapq.heapify(q) # 우선순위(weight) 정렬
    _, node = heapq.heappop(q)
    for nxt_node, weight_to_nxt in graph[node]:
        distances[nxt_node] = min(distances[node]+weight_to_nxt, distances[nxt_node])
        heapq.heappush(q, [distances[nxt_node], nxt_node])

for i in range(1, V+1):
    dist = distances[i]
    if dist == 1e9:
        dist = 'INF'
    print(dist)