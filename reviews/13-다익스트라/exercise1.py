# https://techblog-history-younghunjo1.tistory.com/247

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

print(graph)
def get_closest_node():
    m = Inf
    idx = 0
    for i in range(1, V+1):
        if not visited[i] and distance[i] < m:
            m = distance[i]
            idx = i
    return idx

def dijkstra(start):
    # 시작노드
    distance[start] = 0
    visited[start] = True
    # 인접노드 계산
    for neighbor in graph[start]:
        nxt, weight = neighbor
        distance[nxt] = weight
    
    # 시작 노드 제외한 노드들
    for _ in range(V-1):
        # 방문하지 않았으면서 시작노드와 최단거리인 노드 반환
        current = get_closest_node()
        visited[current] = True
        for nxt_node in graph[current]:
            nxt_node_id, nxt_weight = nxt_node
            distance[nxt_node_id] = min(distance[current] + nxt_weight, distance[nxt_node_id])

dijkstra(1)
# print(distance)
for i in range(1, V+1):
    if distance[i] == Inf:
        print(f"{i} 도달 불가능")
    else:
        print(f"{i} 거리 {distance[i]}")