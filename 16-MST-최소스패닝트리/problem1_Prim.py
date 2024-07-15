# MST ( 최소 스패닝 트리 ) 1197
# https://www.acmicpc.net/problem/1197
# 노드의 개수 N과 링크의 개수 M이 주어집니다.
# M개 만큼 연결되어 있는 노드 A,B와 가중치 C가 주어집니다.
# 모든 노드를 최소 비용(가중치의 합)으로 연결했을 때의 비용을 계산하세요.

# 입력
# 3 3
# 1 2 1
# 2 3 2
# 1 3 3

# 출력
# 3

# 주어진 그래프를 트리로 바꾼다. (싸이클을 끊는다.)
# 단, 되도록 가중치가 높은 링크를 지워 최소의 비용으로 뻗어나가는 트리를 만들어야 한다.

# 프림 다익스트라
# 현재 내 노드 위치에서 이동하기 전에 연결된 선들의 정보를 모두 담는다.
# 이 중 가장 가중치가 낮은 곳으로 간다.

N, M = 3, 3 #map(int, input().split())
links = [[1, 2, 1], [2, 3, 2], [1, 3, 3]] #[list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for link in links:
    a, b, w = link
    graph[a].append((w, b)) # heapq.heappop에서 가중치 기준으로 우선순위를 주도록 weight를 앞에 둔다
    graph[b].append((w, a)) 

# 다익스트라 탐색
import heapq # 우선순위 큐 필요

answer = 0
count = 0
q = [[0,1]] # 1에서 가중치 없이 출발
while q:
    if count == N: # 모든 노드를 다 방문했다
        break
    weight, node = heapq.heappop(q) # heap을 이용하여, 최소비용을 꺼낸다.
    if visited[node] == 0: # 방문한 적이 없다면
        visited[node] = 1
        answer += weight # 가중치 업데이트
        count += 1 # 방문한 노드 갯수 업데이트
        # 새롭게 도착한 노드 기준으로 다음에 갈 수 있는 링크를 저장
        for nxt in graph[node]:
            heapq.heappush(q,nxt)

print(answer)