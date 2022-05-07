num_testcases = int(input()) # number of test cases
for i in range(num_testcases):
    V, E = map(int,input().split()) # cities (Vertex) and pilots (Edges) respectively
    for j in range(E):
        a, b = map(int, input().split())
    print(V-1) # E = V-1 for an undirected tree
