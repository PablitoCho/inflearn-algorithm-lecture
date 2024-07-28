# https://www.acmicpc.net/problem/13023
# 5명의 친구 관계가 존재하는지
import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N)]
visited = [False for _ in range(N)]

found = False

for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

def DFS(node, depth):
    global found, visited
    if depth == 5:
        found = True
        return
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            DFS(neighbor, depth+1)
    # visited[node] = False 줄은 DFS가 노드에서 가능한 모든 경로를 탐색한 후, 
    # 알고리즘이 백트래킹을 통해 해당 노드를 그래프 탐색 과정에서 다른 경로의 일부로 다시 방문할 수 있도록 하기 위해 존재합니다. 
    # 이는 특정 길이의 경로나 사이클을 찾는 문제에서 흔히 사용되는 기술입니다.
    visited[node] = False 

for i in range(N):
    DFS(i, 1)
    if found:
        break
if found:
    print(1)
else:
    print(0)
