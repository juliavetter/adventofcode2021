def neighbors(v: tuple, bound: int) -> list:
    n = []
    if v[0] != 0:
        n.append((v[0]-1, v[1]))
    if v[1] != 0:
        n.append((v[0], v[1]-1))
    if v[0] != bound:
        n.append((v[0]+1, v[1]))
    if v[1] != bound:
        n.append((v[0], v[1]+1))
    return n

# Dijsktra's algorithm, ugh
def shortest_path(grid: list) -> int:
    dist = dict()
    prev = dict()
    Q = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            dist[(i, j)] = float('inf')
            prev[(i, j)] = None
            Q.append((i, j))
    dist[(0, 0)] = 0

    # while we still have vertices to calculate
    while len(Q) != 0:
        # u = vertex in Q with min dist
        mindist = float('inf')
        u = None
        for v in Q:
            if dist[v] < mindist:
                mindist = dist[v]
                u = v
        Q.remove(u)
        for v in neighbors(u, len(grid)):
            if not v in Q:
                continue
            alt = dist[u] + grid[v[0]][v[1]]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    # backtrack to find the path
    v = (len(grid)-1, len(grid)-1)
    S = set()
    while v != None:
        S.add(v)
        v = prev[v]
    total = 0
    S.remove((0, 0))

    # add up the length of the path
    for v in S:
        total += grid[v[0]][v[1]]
    return total


# part 1

grid = []
with open("15.txt") as input:
    for line in input.readlines():
        line = line.strip()
        grid.append([])
        for c in line:
            grid[len(grid)-1].append(int(c))
print(shortest_path(grid))

# part 2

# takes ~4 hours to finish. whatever. 
# initialize a biggrid (5x bigger than grid) with all 0s
SIZE = len(grid) # assume grid is square
biggrid = []
for i in range(5 * SIZE):
    biggrid.append([])
    for j in range(5 * SIZE):
        biggrid[i].append(0)
        try:
            biggrid[i][j] = grid[i][j]
        except:
            pass

# fill in the values
for i in range(5*SIZE):
    for j in range(5*SIZE):
        if i < SIZE and j < SIZE:
            continue
        if i >= SIZE:
            n = biggrid[i-SIZE][j]
        else:
            n = biggrid[i][j-SIZE]
        biggrid[i][j] = n % 9 + 1
        #num = grid[i%SIZE][j%SIZE] + i//SIZE + j//SIZE
print(shortest_path(biggrid))