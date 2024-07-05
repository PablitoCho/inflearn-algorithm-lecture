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

import sys

sys.setrecursionlimit(99999999) # 가능한 재귀 횟수를 올린다. 

# 100 ~ 999
def get_strike(num1, num2):
    strikes = 0
    strnum1 = str(num1)
    for i, num in enumerate(str(num2)):
        if num == strnum1[i]:
            strikes += 1
    return strikes

def get_ball(num1, num2):
    balls = 0
    strnum1 = str(num1)
    for i, num in enumerate(str(num2)):
        if num in strnum1 and num != strnum1[i]:
            balls += 1
    return balls

n = 4 # int(input()) 
hints = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]] # [list(map(int, input().split())) for _ in range(n)]

answer = 0

def recur(idx, number):
    global answer
    if idx == n:
        answer += 1
        # print(f'found answer {number}') # 324, 328
        recur(0, number+1)
        return
    
    if number == 1000:
        return
    
    current_num, strikes, balls = hints[idx]
    if get_strike(number, current_num) == strikes and get_ball(number, current_num) == balls:
        recur(idx+1, number) # 같은 번호를 다음 힌트로 확인한다
    else:
        recur(0, number+1) # 다음 번호를 첫번째 힌트부터 재시작한다.

recur(0, 100) # 0 : 첫번째 힌트부터 시작, 100 : 시작 번호

print(answer)