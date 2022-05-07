import sys

from collections import defaultdict

sys.setrecursionlimit(1000000)

n = int(input()) # 1 <= n <= 100,000
AdjList = defaultdict(lambda : []) # initialize adjacency list
visited = [] # initialize

# Adjacency List
for _ in range(n):
    rule = input().split()
    rule[0] = rule[0][0:-1] # formatting to remove the ':'
    for i in range(1, len(rule)):
        AdjList[rule[i]].append(rule[0]) # appended in traversal direction from the source

source = input()
toposort = [] # initialize

def DFS(source):
    visited.append(source)
    for neighbour in AdjList[source]:
        if neighbour not in visited:
            DFS(neighbour)
            toposort.append(neighbour)
    return reversed(toposort)

ans = DFS(source)
print(source)
for element in ans:
    print(element)
