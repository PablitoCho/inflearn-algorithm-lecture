# https://www.acmicpc.net/problem/15649
N, M = map(int, input().split())
# 1부터 N까지 중복없이 M개를 고른 수열 모두를 출력

# 백트래킹(backtracking)이란? : 해를 찾는 도중 해가 아니어서 막히면, 되돌아가서 다시 해를 찾아가는 기법을 말합니다. 최적화 문제와 결정 문제를 푸는 방법이 됩니다.

def solve1(n): # recursive 함수의 n? depth를 의미!
    if n == M:
        print(*arr)
        return
    for i in range(1, N+1): # 다음 depth로 1부터 N까지 하나씩 넣어준다. (nested 반복문)
        if i in arr: # 중복없이
            continue
        arr.append(i)
        solve(n+1)
        arr.pop() # 재귀함수를 끝내고 돌아왔을 때 다시 빼주어야 한다. arr 배열을 오염시키지 않기 위해 필수..!

# def solve(n):
#     if n == M:
#         print(*arr)
#         return
#     for i in range(1, N+1):
#         if arr and i <= arr[-1]:
#             continue
#         arr.append(i)
#         solve(n+1)
#         arr.pop()
arr = []
solve(0)