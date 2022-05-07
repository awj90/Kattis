m, n = map(int,input().split()) # 1 <= m, n <= 100

grid = [] # initialize

for i in range(m):
    grid.append(list(input()))

delta_m = [-1, -1, -1,  0,  1,  1,  1,  0]
delta_n = [-1,  0,  1,  1,  1,  0, -1, -1]

#from pprint import pprint
#pprint(grid)

def DFS(r, c):
    grid[r][c] = '.'
    for j in range(len(delta_m)):
        new_r = r + delta_m[j]
        new_c = c + delta_n[j]
        if new_r > m-1 or new_r < 0 or new_c > n-1 or new_c < 0: continue # out of grid
        if grid[new_r][new_c] == '#':
            DFS(new_r, new_c)
            break # no two amoebas overlap or touch each other i.e. only 1 DFS neighbour

num_amoebas = 0 # initialize

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == '#':
            num_amoebas += 1
            DFS(row, col)

print(num_amoebas)
