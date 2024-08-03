n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

def DFS(computers, visited, node):
    visited[node] = True
    for idx, connected in enumerate(computers[node]):
        if connected == 1 and not visited[idx]:
            DFS(computers, visited, idx)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            DFS(computers, visited, i)
        answer += 1
    return answer

answer = solution(n, computers)
print(answer)