tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

# 방문하는 공항 경로를 배열에 담아 return
from collections import defaultdict
graph = defaultdict(list)

for ticket in tickets:
    graph[ticket[0]].append(ticket[1])

for airport in graph:
    graph[airport].sort(reverse=True)

answer = []
path = ["ICN"]

while path:
    node = path.pop()
    if node not in graph or len(graph[node]) == 0:
        answer.append(path.pop())
    else:
        path.append(graph[node].pop())

answer[::-1]


