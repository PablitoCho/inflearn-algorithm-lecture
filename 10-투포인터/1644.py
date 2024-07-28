# https://www.acmicpc.net/problem/1644
# 하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다.
# ex. 41 : 2+3+5+7+11+13 = 11+13+17 = 41 (세가지)
# ex. 53 : 5+7+11+13+17 = 53 (두 가지)

N = int(input())

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

primes = []
for k in range(2, N+1):
    if isPrime(k):
        primes.append(k)

# print(primes)

M = len(primes)
left, right = 0, 0

answer = 0
summ = primes[0]
while left <= right:
    if summ > N:
        summ -= primes[left]
        left += 1
    else:
        if summ == N:
            answer += 1
        right += 1
        if right == M:
            break
        summ += primes[right]
        
print(answer)

