# https://www.acmicpc.net/problem/1991
from collections import defaultdict
N = 7 #int(input())
tree = [['A', 'B', 'C'], ['B', 'D', '.'], ['C', 'E', 'F'], ['E', '.', '.'], ['F', '.', 'G'], ['D', '.', '.'], ['G', '.', '.']] 
#[list(input().split()) for _ in range(N)]
# print(tree)

# graph = defaultdict(list)
graph = {}
for node in tree:
    p, c1, c2 = node
    graph[p] = [c1, c2]

def traverse(node):
    if node == '.':
        return
    children = graph[node]
    traverse(children[0])
    print(node)
    traverse(children[1])

traverse('A')