# 최단거리 ( #1753 )
# https://www.acmicpc.net/problem/1753
# 노드와 링크의 개수가 주어집니다. 출발한 노드의 번호가 주어집니다.
# A,B로 가는 링크의 가중치 C가 주어집니다.
# 출발한 노드부터 각각의 노드에 도달하는 최단거리를 계산하세요. (자기 자신으로는 0, 도달 불가능한 곳은 INF)

# 입력
# 5 6
# 1
# 5 1 1
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6

# 출력
# 0
# 2
# 3
# 7
# INF

V, E = 5, 6 #map(int, input().split())
start = 1 #int(input())
edges = [[5, 1, 1], [1, 2, 2], [1, 3, 3], [2, 3, 4], [2, 4, 5], [3, 4, 6]] #[list(map(int, input().split()))for _ in range(E)]

#print(edges)

# BFS와 조금 다를 뿐.. 동일한 방식으로 적용하면 된다
from collections import deque

links = [[] for _ in range(V+1)]
for edge in edges:
    x1, x2, weight = edge
    links[x1].append([x2, weight])

#print(links) # [[], [[2, 2], [3, 3]], [[3, 4], [4, 5]], [[4, 6]], [], [[1, 1]]]


visited = [0 for _ in range(V+1)]
dist = [1e9 for _ in range(V+1)]

q = deque()
q.append(start) # 시작점
dist[start] = 0

# def find_shortest():
#     mini = 1e9
#     idx = 0
#     for i in range(1, V+1):
#         if dist[i] <= mini:
#             idx = i
#             mini = dist[i]
#     return idx


while q:
    node = q.popleft()
    for nxt, w in links[node]:
        # 1. 각 위치의 값을 업데이트한다.
        # 2. 만약 여러 경로가 있다면, 더 작은 수가 업데이트 될때만 업데이트한다
        dist[nxt] = min(dist[node] + w, dist[nxt])
        q.append(nxt)
        visited[nxt] = 1
        # 3. 시작점으로부터 거리를 봐서, 짧은 순서대로 탐색 (otherwise, 이미 방문한 노드를 업데이트해야 하는 오염 발생)
        idx = dist.index(min(dist)) # find_shortest()
        if idx in q:
            q.remove(idx)
            q.appendleft(idx)

print(dist)