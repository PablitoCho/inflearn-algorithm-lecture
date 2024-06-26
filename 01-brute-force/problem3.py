# 백준 #19532
# 숫자 A,B,C,D,E,F
# 다음 연립방정식에서 x와 y값을 계산하는 프로그램을 작성하세요
# Ax + By = C
# Dx + Ey = F
# 범위 : X와 Y는 -10000이상 10000이하 정수

# 입력 1 3 -1 4 1 7
# 출력 2 -1

# 내 코드
# A = int(input())
# B = int(input())
# C = int(input())
# D = int(input())
# E = int(input())
# F = int(input())

# for x in range(-10000, 10001):
#     for y in range(-10000, 10001):
#         if A*x + B*y == C and D*x + E*y == F:
#             print(x, y)
#             break

A,B,C,D,E,F = map(int, input().split()) # 1,3,-1,4,1,7
for x in range(-10000, 10001):
    for y in range(-10000, 10001):
        if A*x + B*y == C:
            if D*x + E*y == F:
                print(x,y)
                break