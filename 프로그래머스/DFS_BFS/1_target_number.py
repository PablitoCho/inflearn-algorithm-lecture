answer = 0
def solution(numbers, target):
    def _DFS(idx, value):
        global answer
        if idx == len(numbers):
            if value == target:
                answer += 1
            return
        nxt = numbers[idx]
        _DFS(idx+1, value + nxt)
        _DFS(idx+1, value - nxt)
    _DFS(0, 0)
    return answer

numbers = [1,1,1,1,1]
target = 3
answer = solution(numbers, target)
print(answer)