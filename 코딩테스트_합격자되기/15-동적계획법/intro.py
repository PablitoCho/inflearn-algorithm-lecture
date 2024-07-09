# 동적 계획법 (Dynamic Programming)
# 전체 문제를 한 번에 해결하는 것이 아니라 작은 부분의 문제를 해결하고, 이것들을 활용하여 전체 문제를 해결하는 방식
# "큰 문제를 작은 문제로 나누었을 때 동일한 작은 문제가 반복해서 등장해야 한다."

# 동적 계획법의 문제 해결 절차
# 1. 문제를 해결하는 해가 있다고 가정
# 2. 종료 조건 설정
# 3. 과정 1, 2를 활용하여 점화식 작성

# 재귀 호출을 줄여주는 메모이제이션
# 이미 계산한 값들을 저장해두었다가 이후 쓸 일이 있는 경우 재활용

N = 10

fibodata = [0 for _ in range(N+1)]

def fibo(n):
    if n < N and fibodata[n] != 0:
        return fibodata[n]
    if n <= 1:
        fibodata[n] = n
        return fibodata[n]
    fibodata[n] = fibo(n-1) + fibo(n-2)
    return fibodata[n]

if __name__ == "__main__":
    print(fibo(N))
    print(fibodata)