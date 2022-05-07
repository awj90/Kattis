from collections import defaultdict, deque
from math import inf
import sys

n, m = map(int, input().split())
target = input().split()
AL = defaultdict(list) 
for _ in range(m):
    l1, l2, c = input().split()
    c = int(c)
    AL[l1].append((l2, c))
    AL[l2].append((l1, c)) # bidirectional, weighted


p = defaultdict(lambda : inf) 
dist = defaultdict(lambda : inf)
p["English"] = dist["English"] = 0 
q = deque(["English"]) 
while q:
    u = q.popleft()
    for v, w in AL[u]:
        if dist[v] == inf:
            dist[v] = dist[u]+1
            p[v] = w # min edge weight to reach v is currently this
            q.append(v)
        elif dist[u]+1 == dist[v]: # already visited before, but with the same distance
            p[v] = min(p[v], w) # take the min cost to reach v with the same distance

for u in target:
    if dist[u] == inf:
        print("Impossible") # not all target languages are reachable
        sys.exit()
print(sum(p.values()))
