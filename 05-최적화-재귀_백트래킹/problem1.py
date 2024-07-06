# 문제 1. 요리사의 고민 ( # 2961 )
# https://www.acmicpc.net/problem/2961
# N개의 재료가 주어집니다.
# 각각의 재료에는 단맛과 짠맛이 있습니다.
# N개의 줄에 재료의 단맛 A와 짠맛 B가 주어집니다.
# 요리에 재료를 추가할 때마다, 재료의 단맛은 기존의 단맛에 더해지고, 짠맛은 기존의 짠맛에 곱해집니다.
# 각 재료는 쓰거나 안 쓸 수 있음. 적어도 하나의 재료는 사용해야 함
# 단맛과 짠맛의 차이가 가장 적은 요리를 만들었을 때, 단맛과 짠맛의 차이를 출력하는 프로그램을 작성하세요.

# 4
# 1 7
# 2 6
# 3 8
# 4 9
# 1

N = 4 # int(input())
ingredients = [[1, 7], [2, 6], [3, 8], [4, 9]] # [list(map(int, input().split())) for _ in range(N)]

def recur(idx, sweet, salt, used):
    global answer
    if idx == N:
        if used == 0:
            return
        # print(f"sweet {sweet} + {ingredient[0]}, salt {salt} * {ingredient[1]}")
        result = abs(sweet - salt)
        answer = min(answer, result)
        return
    ingredient = ingredients[idx]
    recur(idx+1, sweet + ingredient[0], salt * ingredient[1], used+1) # 재료를 사용한 경우
    recur(idx+1, sweet, salt, used) # 사용하지 않는 경우

answer = 99999999999999999999
recur(0, 0, 1, 0)
print(answer)
