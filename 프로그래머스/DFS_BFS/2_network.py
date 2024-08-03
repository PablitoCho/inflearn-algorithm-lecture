n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

# graph = [[] for _ in range(len(computers[0]))]

visited = [False for _ in range(len(computers[0]))]
def DFS(node):
    if visited[node]:
        return
    visited[node] = True
    for k in range(len(computers[0])):
        if k == node:
            continue
        if computers[node][k] == 1:
            DFS(k)

DFS(0)
count = 1
# print(visited)

while True:
    if all(visited):
        break
    nxt = visited.index(False)
    DFS(nxt)
    count += 1

print(count)