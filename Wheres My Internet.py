from collections import deque

N, M = map(int, input().split()) # N: number of vertices, M: number of edges

AdjList = [[] for i in range(N)] # initialize adjacency list
internet_available = [False]*N # initialize

for i in range(M):
    a, b = map(int,input().split()) # adjacent vertices
    AdjList[a-1].append(b-1) # -1 because of 0-indexing in python
    AdjList[b-1].append(a-1) # undirected

# BFS
source = 0 # House number 1 but indexed as 0 is connected
internet_available[source] = True
queue = deque()
queue.append(source)

while queue:
    processing = queue.popleft() # dequeue front of queue and enqueue front element's neighbours
    for neighbour in AdjList[processing]:
        if neighbour in queue or internet_available[neighbour] == True: continue
        queue.append(neighbour)
        internet_available[neighbour] = True

if sum(internet_available) == N:
    print('Connected')
else:
    for i in range(N):
        if not internet_available[i]:
            print(i + 1) # +1 back due to 0 indexing
