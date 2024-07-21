# 문제 4. 숫자야구 ( # 2503 )
# https://www.acmicpc.net/problem/2503

# 입력
# 4
# 123 1 1
# 356 1 0
# 327 2 0
# 489 0 1

# 출력 : 2
N = 4 #int(input())
plays = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]# [list(map(int, input().split())) for _ in range(N)]

def get_strikes_and_balls(num1, num2):
    # num1: answer, num2: play
    strikes = 0
    balls = 0
    num1 = str(num1)
    for i, n in enumerate(str(num2)):
        if n == num1[i]:
            strikes += 1
        elif n in num1:
            balls += 1
    return strikes, balls


answer = 0
def solve(idx, number):
    global answer
    if idx == N:
        answer += 1
        solve(0, number+1)
        return
    if number == 1000:
        return
    num, strikes, balls = plays[idx]
    cal_strikes, cal_balls = get_strikes_and_balls(number, num)
    if strikes == cal_strikes and balls == cal_balls:
        solve(idx+1, number)
    else:
        solve(0, number+1)
    

solve(0, 100) # 첫번째(0) 힌트부터 첫번째 숫자(100)부터 확인하자

print(answer)