from heapq import heappush, heappop
from math import inf

V, E, C, K, M = map(int, input().split())

AL = [[] for i in range(V)] # initialize Adjacency List

# Adjacency List
for i in range(E):
    u, v, w = map(int, input().split()) 
    AL[u-1].append((v-1, w)) # trails are bi-directional
    AL[v-1].append((u-1, w)) # -1 for 0-based indexing
    
# Initialize SSSP outputs and priority queue
D = [inf] * V # initialize list of distances between cottage and each clearing
D[0] = 0 # distance to cottage itself is 0, 0-based indexing for cottage
pq = []
pq.append((D[0], 0))

# SSSP to get shortest distances between cottage and each clearing
while pq:
    d, u = heappop(pq)
    if d > D[u]: continue # not the shortest path
    for v, w in AL[u]:
        if D[u] + w >= D[v]: continue # not the shortest path
        D[v] = D[u] + w # else update with shorter distance to v
        heappush(pq, (D[v],v))

f = list(map(int, input().split())) # list of clearings that have fruits

nearest_clearings = [] # initialize
for clearing in f:
    if D[clearing - 1] == inf: continue # not counted if the fruits are unreachable
    nearest_clearings.append(D[clearing - 1]) # -1 due to 0-based indexing
nearest_clearings_sorted = sorted(nearest_clearings) # list of sorted distances from fruits

if M <= K: # only need to survive until Day M, fruit growth rate doesn't matter
    if len(nearest_clearings_sorted) < M: # not enough reachable fruits initially
        print(-1)
    else:
        print(2*nearest_clearings_sorted[M-1])
elif M > K: # if M is larger than rate of fruit growth, just need to cycle between the K clearings
    if len(nearest_clearings_sorted) < K: # not enough reachable fruits initially
        print(-1)
    else:
        print(2*nearest_clearings_sorted[K-1])
