#문제 4. 2차원 누적합 ( #11660 )
# https://www.acmicpc.net/problem/11660
# 4X4 크기의 표가 주어집니다.
# 직사각형의 좌측 위 좌표와 우측 아래 좌표가 주어졌을 때, 그 범위의 합을 구하는 프로그램을 작성하시오.
# 1	2 3	4
# 2	3 4	5
# 3	4 5	6
# 4	5 6 7
# graph = [list(map(int, input().split())) for _ in range(4)]
# print(graph)
graph = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]

# (x1,y1), (x2, y2)
# x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = 2, 2, 3, 4
prefix = [[0 for _ in range(5)] for _ in range(5)]

for y in range(4):
    for x in range(4):
        prefix[y+1][x+1] = prefix[y][x+1] + prefix[y+1][x] - prefix[y][x] + graph[y][x]
# [[0, 0,  0,  0,  0], 
#  [0, 1,  3,  6,  10],
#  [0, 3,  8,  15, 24],
#  [0, 6,  15, 27, 42],
#  [0, 10, 24, 42, 64]]
print(prefix)
answer = prefix[y2][x2] - prefix[y2][x1-1] + prefix[y1-1][x2] + prefix[y1-1][x1-1]
print(answer)