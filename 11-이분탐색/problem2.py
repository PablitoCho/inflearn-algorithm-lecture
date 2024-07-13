# 나무자르기( #2805 )
# https://www.acmicpc.net/problem/2805
# 정원에 나무들이 있습니다.
# 나무를 자를 때, 나무자르는 기계를 사용할 예정입니다.
# 이 기계는 높이를 설정하면 나무들을 해당 높이로 모두 잘라 버립니다.
# 내가 필요한 나무의 최솟값이 주어졌습니다.
# 내가 필요한 만큼만 나무를 얻기 위한 높이를 계산해주세요.

# 입력
# 4 7
# 20 15 10 17

# 출력
# 15

N, M = 4, 7 #map(int, input().split())
trees = [20, 15, 10, 17] #list(map(int, input().split()))
# print(trees)

s = 1
e = max(trees)

while s <= e: # 교차되기 전까지
    mid = (s+e)//2
    # print(f'current mid: {mid}')
    # 수집되는 나무 계산
    wood = sum([tree - mid for tree in trees if tree > mid])
    if wood >= M : # 많이 채집
        s = mid + 1
    else: # 덜 채집
        e = mid - 1

print(e)

    