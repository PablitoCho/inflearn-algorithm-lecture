# numbers = [1, -1, 2, 3]
from collections import defaultdict

numbers = [-2, -1, 0, 1, 2]

def solution(numbers):
    counts = defaultdict(int)
    answer = 0
    for element in numbers:
        counts[element] += 1
        for two_power in range(21):
            second_element = (1 << two_power ) - element
            answer += counts[second_element]
    return answer

# numbers.sort()

# p1 = 0
# p2 = 0

# answer = 0

# min_pair = 2*numbers[0]
# max_pair = 2*numbers[-1]

# max_e = 0
# while max_pair >= 2**max_e:
#     max_e += 1

# min_e = 0
# while min_pair >= 2**min_e:
#     min_e += 1

# print(min_e, max_e)

# # two pointer
# def _find(value):
#     global answer
#     s, e = 0, len(numbers)-1
#     while s <= e:
#         summ = numbers[s] + numbers[e]
#         # print(f"value {value}")
#         if summ == value:
#             # print(f"  found! {numbers[s]} + {numbers[e]} = {summ}")
#             answer += 1
#             # s += 1
#             e -= 1
#         elif summ < value:
#             s += 1
#         else: # summ > value
#             e -= 1

# for e in range(min_e, max_e):
#     _find(2**e)

# print(answer)
