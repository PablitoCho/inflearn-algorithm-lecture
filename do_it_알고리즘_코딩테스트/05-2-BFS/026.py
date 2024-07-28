# https://www.acmicpc.net/problem/1260
# 주어진 그래프를 DFS와 BFS로 탐색한 결과를 출력하시오

from collections import deque

N, M, start = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
# print(edges)
graph = [[] for _ in range(N+1)]
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

for i in range(N+1):
    graph[i].sort()

visited = [False] * (N+1)
def DFS(node):
    print(node, end=' ')
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            DFS(neighbor)

DFS(start)
print()

visited = [False] * (N+1)
def BFS(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        node = q.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)

BFS(start)
