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

N = int(input())
nodes = [input().split() for _ in range(N)]
graph = {node[0] : [node[1], node[2]] for node in nodes}

# Tree -> DFS를 사용하여 전위순회, 후위순회
#  - 전위순회? 부모의 정보를 자식에게 내려보낸다
#   현재 노드의 정보를 가지고 자식들에게 갈 수 있다.
#   부모로부터의 정보를 순서대로 계산할 때.
#  - 후위순회? 자식들의 정보를 부모에게 올려보낸다.
#   자식의 정보를 계산해서 부모단에서 합쳐야 할 때 사용

# pre-order
# def recur(node):
#     if node == '.':
#         return
#     print(node, end="")
#     recur(graph[node][0]) # left child
#     recur(graph[node][1]) # right child

# post-order
def recur(node):
    if node == '.':
        return
    recur(graph[node][0]) # left child
    recur(graph[node][1]) # right child
    print(node, end="")

# in-order
# def recur(node):
#     if node == '.':
#         return
#     recur(graph[node][0]) # left child
#     print(node, end="")
#     recur(graph[node][1]) # right child

recur('A')