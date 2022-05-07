from collections import deque

def neighbours(N, x, y):
    # returns a list of valid positions a knight can jump to from an initial position (x,y)
    # valid position means not outside the N x N chessboard
    # (x,y) is provided in 0-based index
    dx = [ 2, 2,-2,-2, 1, 1,-1,-1]
    dy = [ 1,-1, 1,-1, 2,-2, 2,-2]
    output = []
    for j in range(len(dx)):
        new_x = x + dx[j]
        new_y = y + dy[j]
        if 0 <= new_x < N and 0 <= new_y < N:
            output.append((new_x, new_y))
    return output

N = int(input()) # chessboard length
chessboard = [] # initialize grid

# Get game grid from user
for i in range(N):
    row = []
    row.extend(input())
    chessboard.append(row)
    if 'K' in row:
        source = (i, row.index('K'))

chessboard[source[0]][source[1]] = 0 # set knight's initial position to 0

# BFS
# BFS works as all neighbours are 1 move away (1 weight)
queue = deque()
queue.append(source) # enqueue initial knight position

while queue:
    front = queue.popleft() # dequeue front of queue
    for neighbour in neighbours(N, front[0], front[1]):
        if chessboard[neighbour[0]][neighbour[1]] == '#': continue # blocked cell
        if chessboard[neighbour[0]][neighbour[1]] == '.': # not visited yet
            queue.append(neighbour) # enqueue neighbour
            chessboard[neighbour[0]][neighbour[1]] = chessboard[front[0]][front[1]] + 1 # +1 distance (move) away
        else: # already visited, update shortest path
            if chessboard[neighbour[0]][neighbour[1]] > chessboard[front[0]][front[1]] + 1:
                chessboard[neighbour[0]][neighbour[1]] = chessboard[front[0]][front[1]] + 1

if chessboard[0][0] == '.':
    print(-1) # not visited
else:
    print(chessboard[0][0]) # 0-based indexing
