from math import inf
from heapq import heappush, heappop

N, S, T = map(int,input().split())

AdjMatrix = [] # initialize

# Adjacency Matrix
for i in range(N):
    row = list(map(int,input().split()))
    AdjMatrix.append(row)

# initialize SSSP outputs (distances) and priority queue
D = [inf] * N
D[S] = 0 # distance from source to itself is 0
priorityq = []
priorityq.append((D[S], S))

while priorityq:
    dist, u = heappop(priorityq)
    if dist > D[u]: continue # not the shortest path
    for v in range(N):
        if AdjMatrix[u][v] == 0: continue # skip (no internal loop)
        if D[v] <= D[u] + AdjMatrix[u][v]: continue # not the shortest path
        D[v] = D[u] + AdjMatrix[u][v]
        heappush(priorityq, (D[v],v))

print(D[T])
