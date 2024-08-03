begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

from collections import defaultdict, deque

# 최소 몇 단계? BFS
graph = defaultdict(list)
distances = defaultdict(int)
visited = defaultdict(bool)


def connected(node1, node2):
    diff = 0
    for ch1, ch2 in zip(node1, node2):
        if ch1 != ch2:
            diff += 1
        if diff > 1:
            return False
    return diff == 1

graph[begin] = [word for word in words if connected(word, begin)]

# print(graph)
for word in words:
    graph[word] = [w for w in words if connected(word, w) and word != w]

print(graph)
q = deque()
q.append(begin)
visited[begin] = True
while q:
    word = q.popleft()
    for nxt in graph[word]:
        # if nxt == 'dog': print(f"{word} > {nxt}")
        if visited[nxt]:
            continue
        visited[nxt] = True
        q.append(nxt)
        distances[nxt] = distances[word] + 1

print(distances)