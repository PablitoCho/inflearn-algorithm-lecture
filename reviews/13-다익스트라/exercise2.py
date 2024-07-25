# https://techblog-history-younghunjo1.tistory.com/248?category=1014800
import heapq
Inf = int(1e9)
# number of vertices and edges
V, E = map(int, input().split()) # 
# 시작 node
start = int(input())
# 5에서 1로 가는 edge 가중치 1
#[list(map(int, input().split())) for _ in range(E)]
edges = [[5, 1, 1], [1, 2, 2], [1, 3, 3], [2, 3, 4], [2, 4, 5], [3, 4, 6]] 

graph = [[] for _ in range(V+1)]
visited =  [False] * (V+1)
distance = [Inf] * (V+1)

for edge in edges:
    x, y, w = edge
    graph[x].append((y,w)) # x -> y with weight w

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # weight가 앞으로..
    distance[start] = 0
    while q:
        weight, node = heapq.heappop(q)
        if distance[node] < weight: # 큐에서 뽑아온 거리가 이미 갱신된 거리보다 크다?
            continue
        for nxt in graph[node]:
            cost = min(distance[node] + nxt[1], distance[nxt[0]])
            distance[nxt[0]] = cost
            heapq.heappush(q, (cost, nxt[0]))

dijkstra(start)
for i in range(1, V+1):
    if distance[i] == Inf:
        print(f"{i} 도달 불가능")
    else:
        print(f"{i} 거리 {distance[i]}")