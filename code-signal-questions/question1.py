# Given an array a, your task is to output an array b of the same length by applying the following transformation: 
# – For each i from 0 to a.length - 1 inclusive, b[i] = a[i - 1] + a[i] + a[i + 1]
# – If an element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, use 0 in its place
# – For instance, b[0] = 0 + a[0] + a[1]

# 4 0 1 -2 3
# [0, 4, 4, 5, 3, 6]

arr = list(map(int, input().split()))

cum_sum = [0 for _ in range(len(arr)+1)]

for i in range(len(arr)):
    cum_sum[i+1] = cum_sum[i] + arr[i]

# print(cum_sum)

def solution(arr):
    cum_sum = [0 for _ in range(len(arr)+1)] # cumulative sum
    for i in range(len(arr)):
        cum_sum[i+1] = cum_sum[i] + arr[i]

    result  = [arr[0] + arr[1]]
    for k in range(3, len(arr)+1):
        result.append(cum_sum[k]-cum_sum[k-3])
    
    result.append(arr[-2] + arr[-1])
    return result

output = solution(arr)
print(output)
