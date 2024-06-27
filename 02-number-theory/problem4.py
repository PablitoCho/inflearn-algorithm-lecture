#문제 4. 공약수 ( #2436 )
# https://www.acmicpc.net/problem/2436
# 두 수 A와 B가 주어졌을 때,
# 두 수의 GCD( 최대공약수 ) 와 LCM ( 최소공배수 ) 를 계산해서 구하시오.
# 30 36
# 6 180

A, B = map(int, input().split())

def _gcd(a,b):
    while a % b != 0:
        tmp = a % b
        a = b
        b = tmp
    return b

def _lcm(a,b):
    return a * b // _gcd(a,b)