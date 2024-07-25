# https://www.acmicpc.net/problem/11725
# 루트없는 트리가 주어진다. 루트가 1이라 할 때, 각 노드의 부모를 구하는 프로그램을 작성하시오

"""
7
1 6
6 3
3 5
4 1
2 4
4 7
"""
N = int(input())
edges = [list(map(int, input().split())) for _ in range(N-1)]
graph = [[] for _ in range(N+1)]
# print(parents)
# 2번 노드부터 부모 노드를 출력하시오
parents = [-1 for _ in range(N+1)]

for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

def recur(node, prev):
    for nxt in graph[node]:
        if nxt == prev:
            continue # 역주행 방지
        recur(nxt, node)
        parents[nxt] = node

recur(1, 0)
# print(parents)
for i in range(2, N+1):
    print(parents[i])