# https://www.acmicpc.net/problem/11724
# 방향없는 그래프가 주어졌을 때, 연결 요소(Connected Component)의 갯수를 구하는 프로그램을 작성하시오
import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]

visited = [False for _ in range(N+1)]

answer = 0

for edge in edges:
    u, v = edge
    graph[u].append(v)
    graph[v].append(u)


def recur(node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            recur(neighbor)

# print(connected)

for k in range(1, N+1):
    if not visited[k]:
        answer += 1
        recur(k)

print(answer)