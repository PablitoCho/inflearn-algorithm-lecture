# 컴퓨터의 갯수 n과 연결 정보 2차원 배열 computers가 주어졌을 때, 네트워크 갯수를 반환하는 함수 solution을 작성하시오

# case1
# n 3
# computers [[1,1,0], [1,1,0], [0,0,1]] # adjacency matrix
# answer 2

# case2
# n 3
# computers [[1,1,0], [1,1,1], [0,1,1]]
# answer 1

n = 3
computers = [[1,1,0], [1,1,1], [0,1,1]]
graph = [[] for _ in range(len(computers))]

for i, links in enumerate(computers):
    for j, link in enumerate(links):
        if i != j and link == 1:
            graph[i].append(j)

# 모든 요소를 탐색. 깊이 우선 방식이 좋다. 왜? 너비 우선 탐색을 해도 되지만,
# 그에 비해 깊이 우선 방식이 구현하기도 더 쉽고 메모리도 적게 사용하기 때문

linked = [False for _ in range(len(computers))]
networks = []

def find_network(start):
    visited = []
    def solve(node):
        if node not in visited:
            visited.append(node)
            linked[node] = True
            for neighbor in graph[node]:
                solve(neighbor)
    solve(start)
    # print(visited)
    networks.append(networks)

for k in range(len(computers)):
    if not linked[k]:
        find_network(k)

print(len(networks))