# case 1. answer 0
# field = [[0, 0, 0],
#          [0, 0, 0],
#          [0, 0, 0],
#          [1, 0, 0],
#          [1, 1, 0]]
# figure = [[0, 0, 1],
#          [0, 1, 1],
#          [0, 0, 1]]
#

# case2. answer 2
# field[row][col]
field =  [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [1, 1, 0, 1, 0],
          [1, 0, 1, 0, 1]]

figure = [[1, 1, 1],
          [1, 0, 1],
          [1, 0, 1]]

row, col = map(int, input().split())
# print(field[x][y])

def solution(field, figure):
    for col in range(0, len(len(field[0]) - len(figure[0]))):
        landed = False
        row = 0
        while not landed:
            copied = field.copy()
            ...        
            

