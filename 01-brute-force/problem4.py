# 문제 4. 숫자야구 ( # 2503 )
# A는 3자리 숫자로 된 정답을 하나 정합니다.
# B는 3자리 숫자를 제시해서 A가 생각하고 있는 정답을 맞히려고 합니다.
# B가 말한 숫자가 정답에 포함되어 있다면 1 Ball입니다.
# B가 말한 숫자가 정답에 포함되어 있고, 자리도 동일하다면 1 Strike입니다.
# 다른 숫자로 이루어진 세 자리수
# Strike와 Ball의 결과를 보고, 가능한 경우의 수 계산하는 프로그램을 작성하세요.

# 4
# 123 1 1
# 356 1 0
# 327 2 0
# 489 0 1
# 2 (왜? 가능한 경우가 324, 328 두 개)

n = int(input()) # 4
hints = [list(map(int, input().split())) for _ in range(n)] # [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]

def strike(num1, num2):
    strikes = 0
    strnum1 = str(num1)
    for i, num in enumerate(str(num2)):
        if num == strnum1[i]:
            strikes += 1
    return strikes

def ball(num1, num2):
    balls = 0
    strnum1 = str(num1)
    for i, num in enumerate(str(num2)):
        if num in strnum1 and num != strnum1[i]:
            balls += 1
    return balls

answer = 0
for i in range(100, 1000):
    flags = []
    for hint in hints:
        num, strickes, balls = hint
        flags.append(
            strike(num, i) == strickes and ball(num, i) == balls)
    if all(flags):
        answer += 1

print(answer)


# if __name__ == "__main__":
#     num1 = 324
#     num2 = 241
#     strikes = strike(num1, num2)
#     balls = ball(num1, num2)
#     print(strikes, balls)