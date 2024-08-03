graph = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']]
start = 'A'

# DFS
from collections import defaultdict
dict = defaultdict(list)
visited = defaultdict(bool)

for edge in graph:
    dict[edge[0]].append(edge[1])

# print(dict) # defaultdict(<class 'list'>, {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'E': ['F']})

def DFS(node):
    if node in visited:
        return
    print(node)
    visited[node] = True
    for neighbor in dict[node]:
        DFS(neighbor)
        
# DFS(start)

from collections import deque

path = [start]
q = deque()
q.append(start)
visited[start] = True
while q:
    node = q.popleft()
    for neighbor in dict[node]:
        if not visited[neighbor]:
            q.append(neighbor)
            visited[neighbor] = True
            # print(neighbor)
            path.append(neighbor)
print(path)