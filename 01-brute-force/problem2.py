# 백준 #14568
# 친구 A,B,C에게 사탕을 나누어주려고 합니다.
# 조건은 아래와 같습니다.
#  1. 남은 사탕이 없어야 함
#  2. A는 B보다 2개 이상 많은 사탕을 가져가야 함
#  3. 셋 중 사탕을 하나도 못 받는 친구는 없어야 함
#  4. C가 받는 사탕은 짝수
# 분배 가능한 경우의 수를 출력
# ex. 사탕 6개 -> 경우의 수 1

# my answer
# candies = int(input())
# count = 0
# for a in range(1, candies+1):
#     for b in range(1, candies - a + 1):
#         c = 6 - (a+b)
#         if c > 0 and c % 2 == 0 and a - b > 1:
#             print(f"a :{a} b :{b} c :{c}")
#             count += 1
# print(count)

candy = int(input()) # 6

answer = 0
for A in range(0, candy+1): # 0개 ~ 6개
    for B in range(0, candy+1):
        for C in range(0, candy+1):
            if A + B + C == candy:
                if A - B >= 2:
                    if A > 0 and B > 0 and C >0:
                        if C % 2 == 0:
                            answer += 1

print(answer)