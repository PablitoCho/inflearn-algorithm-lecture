# case 1
# graph [[1,2],[1,3],[2,4],[2,5],[3,6],[3,7],[4,8],[5,8],[6,9],[7,9]]
# start 1
# return [1,2,3,4,5,6,7,8,9]

# case 2
# graph [[0,1],[1,2],[2,3],[3,4],[4,5][5,0]]
# start 1
# return [1,2,3,4,5,0]

from collections import deque

graph = [[0,1],[1,2],[2,3],[3,4],[4,5], [5,0]]
edges = [[] for _ in range(101)]
visited = []
start = 1

for g in graph:
    a, b = g
    edges[a].append(b)
    edges[b].append(a)

q = deque()
q.append(start)
visited.append(start)

while q:
    node = q.popleft()
    for neighbor in edges[node]:
        if neighbor in visited:
            continue
        visited.append(neighbor)
        q.append(neighbor)

print(visited)