# 최단경로 구하기
# https://www.acmicpc.net/problem/1753

import heapq

V, E = map(int, input().split())
start = int(input())
edges = [list(map(int, input().split())) for _ in range(E)]

graph = [[] for _ in range(V+1)]
for edge in edges:
    u, v, w = edge
    graph[u].append((v, w)) # next node, distance

distances = [float("inf") for _ in range(V+1)]
paths = [[] for _ in range(V+1)]

q = []

distances[start] = 0
paths[start].append(start)

heapq.heappush(q, (distances[start], start))

while q:
    current_distance, current_node = heapq.heappop(q)
    if distances[current_node] < current_distance:
        continue
    for neighbor in graph[current_node]:
        next_node, next_distance = neighbor
        if next_distance < distances[next_node]:
            distances[next_node] = min(distances[current_node] + next_distance, distances[next_node])
            paths[next_node] = paths[current_node] + [next_node]
            heapq.heappush(q, (distances[next_node], next_node))

print(distances)