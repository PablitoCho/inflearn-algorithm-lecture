# https://www.acmicpc.net/problem/1167
from collections import deque

V = int(input())
edges = [list(map(int, input().split())) for _ in range(V)]
tree = [[] for _ in range(V+1)]

for edge in edges:
    node = edge[0]
    edge.pop(0)
    for i in range(len(edge) // 2):
        child, distance = edge[i*2], edge[i*2+1]
        tree[node].append((child, distance))

distances =   [0] * (V+1)
visited = [False] * (V+1)

def BFS(v):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        current = q.popleft()
        for nxt in tree[current]:
            nxt_node, nxt_dist = nxt
            if not visited[nxt_node]:
                visited[nxt_node] = True
                q.append(nxt_node)
                distances[nxt_node] = distances[current] + nxt_dist
BFS(1)
# print(tree)
# print(distances)
start = distances.index(max(distances))
distances =   [0] * (V+1)
visited = [False] * (V+1)

BFS(start)
print(max(distances))
