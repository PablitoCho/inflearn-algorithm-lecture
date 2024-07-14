# https://www.acmicpc.net/problem/2304
# https://www.acmicpc.net/problem/14719
# 막대 기둥의 개수 N이 주어집니다.
# 그리고 기둥의 위치와 높이가 X,Y 좌표로 주어집니다.
# 가장 높은 기둥을 중심으로 텐트의 천을 씌워, 그 텐트가 차지하는 크기를 계산하는 프로그램을 작성하시오
# 7
# 2 4
# 11 4
# 15 8
# 4 6
# 5 3
# 8 10
# 13 6
# 98
# 

# N = int(input())
# pillars = [list(map(int, input().split())) for _ in range(N)]
# https://recordofwonseok.tistory.com/409

# N = 7
# pillars = [[2, 4], [11, 4], [15, 8], [4, 6], [5, 3], [8, 10], [13, 6]]
# pillars = sorted(pillars, key=lambda x:x[0])

# Xs = [pillar[0] for pillar in pillars]
# heights = [pillar[1] for pillar in pillars]
# max_x = Xs[heights.index(max(heights))]

# def findHeightByX(x):
#     ls = [pillar[1] for pillar in pillars if pillar[0] == x]
#     if ls:
#         return ls[0]
#     return 0

# area = 0
# height = heights[0]
# for i in range(Xs[0], max_x+1):
#     current_height = findHeightByX(i)
#     if current_height >= height:
#         height = current_height
#     area += height
# height = heights[-1]
# for i in reversed(range(max_x+1, Xs[-1]+1)):
#     current_height = findHeightByX(i)
#     if current_height >= height:
#         height = current_height
#     area += height
# print(area)


## 세 가지 방법 중 하나로 풀 수 있다.
# 완전탐색
# 누적합
# 투 포인터

# n = int(input())
n = 7
graph = [0]*10001
x_list, y_list = [], []
pillars = [[2, 4], [11, 4], [15, 8], [4, 6], [5, 3], [8, 10], [13, 6]]

for i in range(n):
    x, y = pillars[i]
    graph[x] = y
    x_list.append(x)
    y_list.append(y)

# print(graph)
maxHeight = max(y_list)
maxWidth = max(x_list)

prefix = [0]*(maxWidth+2)
suffix = [0]*(maxWidth+2)

maxPoint = []

#prefix계산
h = 0
for f in range(1,maxWidth+3):
    if(graph[f] == maxHeight):
        maxPoint.append(f)
        break
    h = max(h, graph[f])
    prefix[f] = prefix[f-1] + h

h = 0
for b in range(maxWidth,0,-1):
    if(graph[b] == maxHeight):
        maxPoint.append(b)
        break
    h = max(h, graph[b])
    suffix[b] = suffix[b+1] + h

print(prefix)
print(suffix)