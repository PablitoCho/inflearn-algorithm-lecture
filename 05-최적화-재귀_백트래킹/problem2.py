# 문제 2. 요리사의 복잡한 고민 ( #19942 )
# https://www.acmicpc.net/problem/19942
# N개의 재료가 주어집니다.
# 그 다음 채워야 하는 영양소 a,b,c,d가 주어집니다.
# 각각의 재료에는 영양소가 있습니다.
# N개의 줄에 재료의 단백질 A와 지방 B 탄수화물 C 비타민 D 가격 E 가 주어집니다.
# 요리에 재료를 추가할 때마다, 영양소는 기존의 영양소에 더해집니다.
# 가장 싼 가격으로 원하는 영양소를 모두 채웠다고 했을 때, 그 가격을 계산하는 프로그램을 작성하시오.

# 6
# 100 70 90 10
# 30 55 10 8 100
# 60 10 10 2 70
# 10 80 50 0 50
# 40 30 30 8 60
# 60 10 70 2 120
# 20 70 50 4 4
# 134

N = 6 #int(input())
A, B, C, D = 100, 70, 90, 10
ingredients = [[30, 55, 10, 8, 100], [60, 10, 10, 2, 70], [10, 80, 50, 0, 50], [40, 30, 30, 8, 60], [60, 10, 70, 2, 120], [20, 70, 50, 4, 4]] # [list(map(int, input().split())) for _ in range(N)]

answer = 99999999999999

def recur(idx, a, b, c, d, price):
    global answer
    if idx == N:
        if a < A or b < B or c < C or d < D:
            return
        answer = min(price, answer)
        return
    _a, _b, _c, _d, _price = ingredients[idx]
    # 재료를 사용한 경우
    recur(idx+1, a+_a, b+_b, c+_c, d+_d, price + _price)
    # 재료를 사용하지 않은 경우
    recur(idx+1, a, b, c, d, price)

recur(0, 0, 0, 0, 0, 0)

print(answer)