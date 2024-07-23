## recursive
n = int(input())

# naive recursive algorithm. drawback is that it requires computing the same Fibonacci numbers multiple times
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-2) + fibonacci(n-1)

# Top-Down DP
# dp = [-1 for _ in range(n+1)]
# def fibonacci(n):
#     if n <= 1:
#         dp[n] = n
#         return n
#     if dp[n] > -1:
#         return dp[n]
#     dp[n] = fibonacci(n-1) + fibonacci(n-2)
#     return dp[n]

# Bottom-Up DP
def fibonacci(n):
    if n <= 1:
        return n
    a = 0 # 0th seq
    b = 1 # 1st seq
    for i in range(2, n):
        temp = a+b
        # print(f'{i}th number. {a} + {b} = {temp}')
        a = b
        b = temp
    return a + b


result = fibonacci(n)
print(f"fibonacci({n}) is {result}")