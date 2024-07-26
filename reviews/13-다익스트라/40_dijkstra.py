# 주어진 노드와 시작 노드를 이용하여 다익스트라 알고리즘을 구현하는 solution() 함수를 작성하세요
# case1
# graph : {'A':{'B':9, 'C':3}, 'B':{'A':5}, 'C':{'B':1}}
# start : 'A'
# return [
#   {'A':0, 'B':4, 'C':3},
#   {'A':['A'], 'B':['A', 'C', 'B'], 'C':['A', 'C']}
# ]

# case2
# graph : {'A':{'B':1}, 'B':{'C':5}, 'C':{'D':1}, 'D':{}}
# start : 'A'
# return [
#   {'A':0, 'B':1, 'C':6, 'D':7},
#   {'A':['A'], 'B':['A','B'], 'C':['A','B','C'], 'D':['A','B','C','D']}
# ]

graph = {'A':{'B':9, 'C':3}, 'B':{'A':5}, 'C':{'B':1}}
start = 'A'

# distances = {'A':float("inf"), 'B':float("inf"), 'C':float("inf")}
# paths = {'A':[], 'B':[], 'C':[]}

import heapq

def solution(graph, start):
    distances = {node:float("inf") for node in graph}

    # 시작 노드 초기화
    distances[start] = 0
    paths = {start:[start]}
    
    q = []
    heapq.heappush(q, (distances[start], start))
    
    while q:
        # 현재 가장 거리 값이 적은 노드를 가져온다
        current_distance, current_node = heapq.heappop(q)
        # 만약 가져온 거리가 큐에서 가져온 거리보다 크면, 해당 노드는 이미 처리한 것이므로 무시
        if distances[current_node] < current_distance:
            continue
        # 현재 노드와 인접한 노드들의 거리 값을 계산하여 업데이트
        for next_node in graph[current_node]:
            next_distance = graph[current_node][next_node]
            # 거리가 계산된 거리보다 작은 경우만 최소 비용 및 최단 경로 업데이트
            if next_distance < distances[next_node]:
                distances[next_node] = min(distances[next_node], distances[current_node] + next_distance)
                paths[next_node] = paths[current_node] + [next_node]
                heapq.heappush(q, (distances[next_node], next_node))
    return paths, distances

paths, distances = solution(graph, start)
print(paths, distances)