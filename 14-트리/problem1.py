# 트리 순회 ( #1991 )
# https://www.acmicpc.net/problem/1991
# 노드 A와 LEFT, RIGHT 순서대로 트리가 주어집니다.
# 해당 트리를 전위순회, 중위순회, 후위순회 하였을 때의 결과를 출력하세요.

# [입력]
# 7
# A B C
# B D .
# C E F
# E . .
# F . G
# D . .
# G . .

# [출력]
# ABDCEFG
# DBAECFG
# DBEGFCA

N = 7#int(input()) # 노드 갯수
nodes = [['A', 'B', 'C'], ['B', 'D', '.'], ['C', 'E', 'F'], ['E', '.', '.'], ['F', '.', 'G'], ['D', '.', '.'], ['G', '.', '.']] #[list(map(str, input().split())) for _ in range(N)]

graph = [[] for _ in range(130)] # 넉넉한 사이즈로..

for node in nodes:
    a,b,c = node
    # 아스키코드 변환
    a = ord(a)
    b = ord(b)
    c = ord(c)
    graph[a].append(b)
    graph[a].append(c)

#print(graph) # [..., [66, 67], [68, 46], [69, 70], [46, 46], [46, 46], [46, 71], [46, 46], ...]

# DFS (전위순회)
# def recur(node):
#     if node == 46: # .
#         return
#     print(chr(node), end="") # 아스키 > character
#     recur(graph[node][0]) # 왼쪽 탐색
#     recur(graph[node][1]) # 오른쪽 탐색

# DFS (후위순회)
# def recur(node):
#     if node == 46: # .
#         return
#     recur(graph[node][0]) # 왼쪽 탐색
#     recur(graph[node][1]) # 오른쪽 탐색
#     print(chr(node), end="") # 아스키 > character

# DFS (중위순회) - 이진트리인 경우에만 의미있음.. 실제로 사용하는 일도 없다.
def recur(node):
    if node == 46: # .
        return
    recur(graph[node][0]) # 왼쪽 탐색
    print(chr(node), end="") # 아스키 > character
    recur(graph[node][1]) # 오른쪽 탐색

recur(ord('A'))

