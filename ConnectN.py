def check_horizontal_win(r, c, N, game_grid):
# checks for consecutive colours horizontally rightwards from a starting point (r, c)
# returns True if horizontal win exists, else returns False
    colour = game_grid[r][c]
    if len(game_grid[0]) < c + N:
        return False # not possible to win horizontally, will extend beyond game grid
    for i in range(1,N):
       if game_grid[r][c + i] != colour:
           return False
    return True

def check_vertical_win(r, c, N, game_grid):
# checks for consecutive colours vertically downwards from a starting point (r, c)
# returns True if vertical win exists, else returns False
    colour = game_grid[r][c]
    if len(game_grid) < r + N:
        return False # not possible to win vertically, will extend beyond game grid
    for j in range(1,N):
       if game_grid[r + j][c] != colour:
           return False
    return True

def check_descending_diagonal_win(r, c, N, game_grid):
# checks for consecutive colours diagonally descending rightward from a starting point (r, c)
# returns True if diagonal win exists, else returns False
    colour = game_grid[r][c]
    if len(game_grid[0]) < c + N or len(game_grid) < r + N:
        return False # not possible to win diagonally, will extend beyond game grid
    for k in range(1,N):
       if game_grid[r + k][c + k] != colour:
           return False
    return True

def check_ascending_diagonal_win(r, c, N, game_grid):
# checks for consecutive colours diagonally ascending rightward from a starting point (r, c)
# returns True if diagonal win exists, else returns False
    colour = game_grid[r][c]
    if len(game_grid[0]) < c + N or (r - N + 1 < 0):
        return False # not possible to win diagonally, will extend beyond game grid
    for k in range(1,N):
       if game_grid[r - k][c + k] != colour:
           return False
    return True

import sys

X, Y, N = map(int, input().split())
game_grid = [] # initialize
winner = {'R': 'RED WINS', 'B': 'BLUE WINS'}

for _ in range(X):
    game_grid.append(input().split())

for row in range(X):
    for col in range(Y):
        if game_grid[row][col] == 'O': continue # skip
        if check_horizontal_win(row, col, N, game_grid) or check_vertical_win(row, col, N, game_grid) or check_descending_diagonal_win(row, col, N, game_grid) or check_ascending_diagonal_win(row, col, N, game_grid):
            print(winner[game_grid[row][col]])
            sys.exit()

print('NONE')
