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
import heapq # 우선순위 큐 사용

links = [[] for _ in range(V+1)]
for edge in edges:
    x1, x2, weight = edge
    links[x1].append([x2, weight])

#print(links) # [[], [[2, 2], [3, 3]], [[3, 4], [4, 5]], [[4, 6]], [], [[1, 1]]]


dist = [1e9 for _ in range(V+1)]

q = []
# q.append([0, start]) # 거리와 시작점
heapq.heappush(q, [0, start])
dist[start] = 0

while q:
    # 우선순위 큐를 이용하여 거리로 정렬한다.
    heapq.heapify(q) # heapfy (힙한 상태로 정렬!)
    # node = q.pop(0) # pop후에는 heap 상태가 무너진다
    _, node = heapq.heappop(q)
    for nxt, w in links[node]:
        # 1. 각 위치의 값을 업데이트한다.
        # 2. 만약 여러 경로가 있다면, 더 작은 수가 업데이트 될때만 업데이트한다
        if dist[node] + w < dist[nxt]:
            dist[nxt] = min(dist[node] + w, dist[nxt])
        # q.append([dist[nxt], nxt])
        heapq.heappush(q, [dist[nxt], nxt])

print(dist)