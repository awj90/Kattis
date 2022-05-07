# DFS
def DFS(u):
    visited[u] = True # global
    for neighbour in AdjList[u]:
        if not visited[neighbour]:
            DFS(neighbour)

num_testcases = int(input()) # number of test cases

for _ in range(num_testcases):

    n, m, l = map(int,input().split()) # n: num of domino tiles
    AdjList = [[] for i in range(n)] # initialize adjacency list
    visited = [False] * n # initialize, True if domino falls
    
    # consolidate an adjacency list first
    for i in range(m):
        x, y = map(int,input().split()) # adjacent vertices
        AdjList[x-1].append(y-1) # -1 because of 0-indexing in python

    # DFS
    for j in range(l):
        source = int(input()) - 1 # -1 because of 0-indexing in python
        DFS(source)

    print(sum(visited))

'''
BFS version

from collections import deque

num_testcases = int(input()) # number of test cases

for _ in range(num_testcases):

    n, m, l = map(int,input().split()) # n: num of domino tiles
    AdjList = [[] for i in range(n)] # initialize adjacency list
    visited = [False] * n # initialize, True if domino falls
    
    # consolidate an adjacency list first
    for i in range(m):
        x, y = map(int,input().split()) # adjacent vertices
        AdjList[x-1].append(y-1) # -1 because of 0-indexing in python

    # BFS
    for j in range(l):
        source = int(input()) - 1 # -1 because of 0-indexing in python
        visited[source] = True
        queue = deque()
        queue.append(source)
        while queue:
            processing = queue.popleft() # dequeue first element and enqueue the first element's neighbours (if any)
            for neighbour in AdjList[processing]:
                if neighbour in queue: continue
                queue.append(neighbour)
                visited[neighbour] = True
    print(sum(visited))

'''
