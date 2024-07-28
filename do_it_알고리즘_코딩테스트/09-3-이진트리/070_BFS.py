# https://www.acmicpc.net/problem/1991
N = 7 #int(input())
tree = [['A', 'B', 'C'], ['B', 'D', '.'], ['C', 'E', 'F'], ['E', '.', '.'], ['F', '.', 'G'], ['D', '.', '.'], ['G', '.', '.']] 
#[list(input().split()) for _ in range(N)]
# print(tree)

# graph = defaultdict(list)
graph = {}
for node in tree:
    p, c1, c2 = node
    graph[p] = [c1, c2]

from collections import deque

q = deque()
q.append('A')
while q:
    node = q.popleft()
    if node == '.':
        continue
    print(node)
    c1, c2 = graph[node]
    q.append(c1)
    q.append(c2)