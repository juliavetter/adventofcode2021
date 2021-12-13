points = set()

def fold(points: set, z: int, axis: str) -> None:
    if axis == 'x':
        a = 0
    elif axis == 'y':
        a = 1
    b = a ^ 1 # b = a xor 1
    tpoints = points.copy()
    for point in tpoints:
        if point[a] < z:
            continue
        else:
            points.discard(point)
            if axis == 'x':
                point = (z - (point[a] - z), point[b])
            elif axis == 'y':
                point = (point[b], z - (point[a] - z))
            points.add(point)

with open("13.txt") as input:
    folding = False
    folds = 0
    for line in input.readlines():
        if folds == 1:
            print("Part 1:", len(points))
        if folding:
            axis = line.split("=")[0][-1]
            coord = int(line.split("=")[1].strip())
            fold(points, coord, axis)
            folds += 1
        elif line == "\n":
            folding = True
        else:
            x = line.split(",")[0].strip()
            y = line.split(",")[1].strip()
            points.add((int(x), int(y)))

# part 2
# print out the points to a grid

# determine the grid dimensions
max_x = 0
max_y = 0
for point in points:
    max_x = max(max_x, point[0])
    max_y = max(max_y, point[1])
# intialize the grid
grid = []
for i in range(max_y+1):
    grid.append([])
    for j in range(max_x+1):
        grid[i].append(" ")
# add points to the grid
for point in points:
    grid[point[1]][point[0]] = "@"
# print out the grid
for i in range(len(grid)):
    for j in range(len(grid[i])):
        print(grid[i][j], end="")
    print("") # new line