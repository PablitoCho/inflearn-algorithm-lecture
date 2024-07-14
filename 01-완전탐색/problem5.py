# 문제 5. 모이기 ( # 1090 )
# N명의 학생들이 모각코를 하기 위해서 한 곳에서 모이려고 합니다.
# 학생들은 어디에 모여도 괜찮으나, 모든 사람들의 이동 거리를 합쳤을 때, 가장 적은 이동 거리였으면 좋겠다고 주장합니다.
# N명의 학생의 집의 위치가 Y, X 2차원으로 주어졌을 때,
# 1,2,3, …, N명의 학생들이 모일 수 있는 최소 거리를 계산하는 프로그램을 작성하세요.

# 조건
#  - N - 50 이하의 수
#  - X,Y좌표는 1_000_000이하의 수
# 4
# 15 14 - A 짱구
# 15 16 - B 철수
# 14 15 - C 맹구
# 16 15 - D 유리
# 0 2 3 4

# 방법1)
# 모든 위치에서 모든 친구들의 거리를 계산해서 가장 적은 값을 알려준다
# X, Y 각각 계산한 후, 합쳐서 최솟값을 알려준다

# 방법2)
# 우리가 한 곳에서 모일 때, 비용을 최소화하기 위해서는 우리의 집 중 한곳에서 모이면 된다.

n = int(input()) # n
coords = [list(map(int, input().split())) for _ in range(n)]
# print(n, coords)

Xs = set([coord[0] for coord in coords])
Ys = set([coord[1] for coord in coords])

def cal_distance(coord1, coord2):
    cal = abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])
    print(f'  calculated {cal}')
    return cal

curr = 1000
found = []
for x in Xs:
    for y in Ys:
        dist = 0
        for c in zip(Xs, Ys):
            dist += cal_distance((x,y), c)
        print(f"x {x} y {y} dist {dist}")
        if dist < curr:
            curr = dist
            found = (x, y)

print(curr, found)

# if __name__ == "__main__":
#     a = [1,2,3]
#     b = [4,5,6]
#     for v in zip(a,b):
#         print(v)

