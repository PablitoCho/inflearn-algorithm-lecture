# https://www.acmicpc.net/problem/1916
import heapq

N = int(input()) # 도시 갯수
M = int(input()) # 버스 갯수

buses = [list(map(int, input().split())) for _ in range(M)] # 출발 도시, 도착 도시 -> 비용

start, end = map(int, input().split())

graph = [[] for _ in range(N+1)]
for bus in buses:
    x, y, d = bus # 출발, 도착, 거리
    graph[x].append((y, d))

distances = [float("inf") for _ in range(N+1)]
q = []

distances[start] = 0
heapq.heappush(q, (distances[start], start))

while q:
    current_distance, current_node = heapq.heappop(q)
    if distances[current_node] < current_distance:
        continue
    for neighbor in graph[current_node]:
        next_node, next_distance = neighbor
        print(neighbor)
        if distances[next_node] > next_distance:
            distances[next_node] = min(distances[current_node] + next_distance, distances[next_node])
            heapq.heappush(q, (distances[next_node], next_node))

print(distances[end])
