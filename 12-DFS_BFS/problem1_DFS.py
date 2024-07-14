# 바이러스( #2606 )
# https://www.acmicpc.net/problem/2606
# 노드와 간선이 주어집니다.
# 아래 그림과 같이 점들이 연결된 관계가 주어졌을 때, 1번 노드가 바이러스에 감염되었다면, 연결된 점들은 모두 바이러스에 감염됩니다.
# 입력이 주어졌을 때, 1번 노드와 연결되어 감염된 노드들의 수를 출력하시오.

# 입력
# 7 # 컴퓨터(노드)의 수 (1 <= n <= 100)
# 6 # 간선의 갯수
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

# 출력
# 4

N = 7 #int(input())
E = 6 #int(input())

graph = [[] for _ in range(N+1)]
# graph[1] = [2, 5], graph[2] = [1,3,5], ...

nodes = [[1, 2], [2, 3], [1, 5], [5, 2], [5, 6], [4, 7]] #[list(map(int, input().split())) for _ in range(E)]

for node in nodes:
    a, b = node
    graph[a].append(b)
    graph[b].append(a)


# DFS 탐색
visited = [0 for _ in range(N+1)]
def recur(node):
    if visited[node] == 1:
        return
    visited[node] = 1
    # print(node)
    for nxt in graph[node]:
        recur(nxt)

recur(1)

print(sum(visited)-1)
