# https://www.acmicpc.net/problem/2961

# N 재료의 갯수
N = 4 #int(input())
# 각 재료의 신맛과 쓴맛
ingredients = [[1, 7], [2, 6], [3, 8], [4, 9]] #[list(map(int, input().split())) for _ in range(N)]



def solve(idx, sour, bitter, used):
    global answer
    if idx == N:
        if used == 0:
            return
        result = abs(sour - bitter)
        answer = min(answer, result)
        return
    ingredient = ingredients[idx]
    # use
    solve(idx+1, sour * ingredient[0], bitter + ingredient[1], used+1)
    # not use
    solve(idx+1, sour, bitter, used)

answer = 99999999
solve(0, 1, 0, 0)
print(answer)