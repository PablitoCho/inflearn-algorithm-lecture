# 피로도 탐색
# 던전마다 탐험을 위해 필요한 최소 필요도와 소모 필요도가 정의
# 최소 필요도 80, 소모 필요도 20의 던전은 80이상의 피로도가 필요하며 탐험 후에는 20의 피로도가 감소됨

# 유저의 현재 피로도 k와 각 던전별 최소 필요 피로도, 소모 피로도가 담김 2차원 배열이 주어진다.
# 유저가 탐험할 수 있는 최대 던전 수를 반환하는 solution() 함수를 완성하시오

# k = 80
# dungeons = [[80,20], [50,40], [30,10]]
# result : 3

k = 80
dungeons = [[80,20], [50,40], [30,10]]

# 백트래킹을 위한 DFS
def dfs(cur_k, cnt, dungeons, visited):
    answer_max = cnt
    for i, dungeon in enumerate(dungeons):
        # 현재 피로도가 최소 필요도보다 높고, 방문한적이 없는 dungeon이라면?
        if cur_k >= dungeon[0] and visited[i]==0:
            visited[i] = 1
            answer_max = max(
                answer_max,
                dfs(cur_k - dungeon[1], cnt+1, dungeons, visited)
            )
            visited[i] = 0
    return answer_max

def solution(k, dungeons):
    visited = [0] * len(dungeons)
    return dfs(k, 0, dungeons, visited)

print(solution(k, dungeons))