# https://www.acmicpc.net/problem/10815

N = int(input())
cards = list(map(int, input().split()))
cards = sorted(cards)

M = int(input())
numbers = list(map(int, input().split()))

# print(cards, numbers)
answer = [0 for _ in range(M)]

for idx, number in enumerate(numbers):
    start, end = 0, N-1
    found = False
    while start <= end:
        mid = (start+end)//2
        if cards[mid] == number:
            found = True
            break
        elif cards[mid] > number:
            end = mid - 1
        else: # cards[mid] < number
            start = mid + 1
    if found == True:
        answer[idx] = 1

print(answer)