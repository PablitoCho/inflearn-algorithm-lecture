# 1부터 N까지 숫자 중 합이 10이 되는 조합 구하기
# 정부 N을 입력받아 1부터 N까지의 숫자 중에서 합이 10이 되는 조합을 리스트로 반환하는 solution() 함수를 작성하시오
# 1) 백트래킹 사용
# 2) 숫자 조합은 오름차순으로
# 3) 같은 숫자는 한 번만 선택 가능
# 4) N은 1 이상 10 이하 정수

# N : 5 [[1,2,3,4], [1,4,5], [2,3,5]]

N = int(input())

def solution(n):
    results = []
    def _backtrack(sum, selected_nums, start):
        # print(f"sum {sum}, selected_nums {selected_nums} start {start}")
        if sum == 10:
            # print(f"sum 10! {selected_nums}")
            results.append(selected_nums)
            return
        
        for i in range(start, n+1):
            if sum + i <= 10:
                _backtrack(sum+i, selected_nums + [i], i+1)
    
    _backtrack(0, [], 1)
    return results




print(solution(N))