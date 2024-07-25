# https://www.acmicpc.net/problem/1753

V, E = map(int, input().split())
start = int(input())
edges = [list(map(int, input().split())) for _ in range(E)]

#print(edges) # [[5, 1, 1], [1, 2, 2], [1, 3, 3], [2, 3, 4], [2, 4, 5], [3, 4, 6]]

# 일종의 BFS
from collections import deque

graph = [[] for _ in range(V+1)]
for edge in edges:
    x, y, w = edge
    graph[x].append((y,w))

visited = [False for _ in range(V+1)]
distances = [1e9 for _ in range(V+1)]

q = deque()
q.append(start)
visited[start] = True
distances[start] = 0

while q:
    node = q.popleft()
    for nxt in graph[node]:
        nxt_node, weight_to_nxt = nxt
        distances[nxt_node] = min(distances[node] + weight_to_nxt, distances[nxt_node])
        q.append(nxt_node)
        visited[nxt_node] = True
        min_idx = distances.index(min(distances)) # 가장 짧은 거리의 index
        if min_idx in q:
            q.remove(min_idx)
            q.popleft(min_idx)

print(distances)
