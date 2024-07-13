# 이분탐색 ( Binary Search )
# https://www.acmicpc.net/problem/10815
# 업다운 게임
# 숫자 찾기 ( #10815 )
# 1개의 수열과 찾아야 할 숫자들이 주어집니다.
# 첫번째 수열에, 찾아야할 숫자들이 포함되어 있는지를 출력하세요.

# 입력
# 5
# 6 3 2 10 -10
# 8
# 10 9 -5 2 3 4 5 -10

# 출력
# 1 0 0 1 1 0 0 1


N = 5 #int(input())
arr1 = [6, 3, 2, 10, -10] # list(map(int, input().split()))
M = 8 #int(input())
arr2 = [10, 9, -5, 2, 3, 4, 5, -10] # list(map(int, input().split()))

# 이분 탐색을 위해(up/down 타노스) 정렬을 해야 한다
arr1 = sorted(arr1)

answer = [0 for _ in range(M)]
for idx, number in enumerate(arr2):
    s, e = 0, N-1
    flag = False
    while s <= e:
        mid = (s+e) // 2
        # up? down? hit?
        if arr1[mid] == number:
            # 정답
            flag = True
            break
        elif arr1[mid] > number: # down
            e = mid - 1
        else: # arr[mid] < number
            s = mid + 1
    if flag:
        answer[idx] = 1

print(answer)