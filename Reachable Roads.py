def DFS(u):
    visited[u] = True
    for neighbour in AL[u]:
        if not visited[neighbour]:
            DFS(neighbour)

n = int(input()) # number of cities n, 1 <= n <= 100

for _ in range(n):
    N = int(input()) # number of road endpoints (vertices)
    M = int(input()) # number of roads (edges)
    AL = [[] for i in range(N)] # initialize adjacency list
    visited = [False] * N # initialize

    for j in range(M):
        u, v = map(int,input().split()) # already 0-index based as mention in question
        AL[u].append(v)
        AL[v].append(u) # undirected graph

    num_CC = 0 # initialize

    for k in range(N):
        if not visited[k]:
            num_CC += 1
        DFS(k)

    print(num_CC - 1) # minimum number of roads to connect x components is x - 1
        
