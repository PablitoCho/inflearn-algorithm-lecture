# https://www.acmicpc.net/problem/19942

# 입력
# 6
# 100 70 90 10
# 30 55 10 8 100
# 60 10 10 2 70
# 10 80 50 0 50
# 40 30 30 8 60
# 60 10 70 2 120
# 20 70 50 4 4

# 출력
# 134 - 최소 비용
# 2 4 6 - 사용된 식재료의 번호 (1부터 시작)

N = 6 #int(input()) # 재료의 갯수
mp, mf, mc, mv = 100, 70, 90, 10 # map(int, input().split())
ingredients = [[30, 55, 10, 8, 100], [60, 10, 10, 2, 70], [10, 80, 50, 0, 50], [40, 30, 30, 8, 60], [60, 10, 70, 2, 120], [20, 70, 50, 4, 4]] #[list(map(int, input().split())) for _ in range(N)]
ingredients = [[]] + ingredients
answer = 999999999
min_indices = []

def solve(idx, protein, fat, carbon, vitamin, price, used):
    global answer, min_indices
    if idx == N+1:
        if protein >= mp and fat >= mf and carbon >= mc and vitamin >= mv:
            if price < answer:
                answer = min(price, answer)
                min_indices = used
        return
    p, f, c, v, pv = ingredients[idx]
    # use
    solve(idx+1, protein+p, fat+f, carbon+c, vitamin+v, price+pv, used + [idx])
    # not use
    solve(idx+1, protein, fat, carbon, vitamin, price, used)

solve(1, 0, 0, 0, 0, 0, [])

print(answer)
print(min_indices)
