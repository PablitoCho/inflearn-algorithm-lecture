# https://www.acmicpc.net/problem/2023
# 신기한 소수
# 7331, 733,  73, 7 모두 소수
import sys
sys.setrecursionlimit(10000)
N = int(input()) # N자리의 수 중 신기한 소수를 모두 찾아 출력하시오

answer = []
def DFS(number):
    if len(str(number)) == N:
        # print(number) # found
        answer.append(number)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            if prime(number * 10 + i):
                DFS(number * 10 + i)

def prime(n):
    for i in range(2, int( n ** 0.5 + 1 )):
        if n % i == 0:
            return False
    return True

DFS(2)
DFS(3)
DFS(5)
DFS(7)

answer.sort()
for n in answer:
    print(n)