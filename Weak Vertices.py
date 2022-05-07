def is_weakvertex(V, AdjList): # returns True if a vertex V is weak given an adjacency list else False
    for neighbour in AdjList[V]:
        if neighbour != V:
            for neighbour_of_neighbour in AdjList[neighbour]:
                if neighbour_of_neighbour != V and neighbour_of_neighbour != neighbour and V in AdjList[neighbour_of_neighbour]:
                    return False
    return True

while True:
    n = int(input()) # number of vertices, 1 <= n <= 20
    if n == -1: break # end

    weak_vertices = [] # initialize output

    AL = [] # initialize adjacency list
    for i in range(n):
        row = list(map(int, input().split()))
        vertice_neighbours = [] # initialize
        for j in range(n):
            if row[j] == 1:
                vertice_neighbours.append(j)
        AL.append(vertice_neighbours) #adjacency llist of neighbours for each vertex

    # Check for weak vertices
    for k in range(n):
        if is_weakvertex(k, AL): # if weak vertex, append to output
            weak_vertices.append(k)

    print(*weak_vertices)
