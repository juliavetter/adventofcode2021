cave = []
with open("9.txt") as input:
    for line in input.readlines():
        cave.append(list())
        for c in line:
            if c != '\n':
                cave[len(cave)-1].append(int(c))

# part 1
total = 0
for i in range(len(cave)):
    for j in range(len(cave[i])):
        current = cave[i][j]
        # check left
        if j != 0 and current >= cave[i][j-1]:
            continue
        # check right
        if j != len(cave[i]) - 1 and current >= cave[i][j+1]:
            continue
        # check up
        if i != 0 and current >= cave[i-1][j]:
            continue
        # check down
        if i != len(cave) - 1 and current >= cave[i+1][j]:
            continue
        total += current + 1
print(total)

#part 2
marked = []
for row in cave:
    marked.append(list())
    for loc in row:
        if loc == 9:
            marked[len(marked)-1].append(True)
        else:
            marked[len(marked)-1].append(False)

# return true iff every element in marked is True
def fully_marked(marked: list) -> bool:
    for row in marked:
        for loc in row:
            if not loc:
                return False
    return True

basins = []
while not fully_marked(marked):
    basin_size = 0
    tosearch = list()

    # find an unmarked point, add it to tosearch
    done = False
    for i in range(len(marked)):
        if done:
            break
        for j in range(len(marked[i])):
            if not marked[i][j]:
                tosearch.append((i, j))
                marked[i][j] = True
                done = True
                break
                
    # use a depth first search to find all reachable unmarked points, keeping track of the number of points reached
    while len(tosearch) != 0:
        i, j = tosearch.pop()
        basin_size += 1
        # check left
        if j != 0 and not marked[i][j-1]:
            tosearch.append((i, j-1))
            marked[i][j-1] = True
        # check right
        if j != len(marked[i]) - 1 and not marked[i][j+1]:
            tosearch.append((i, j+1))
            marked[i][j+1] = True
        # check up
        if i != 0 and not marked[i-1][j]:
            tosearch.append((i-1, j))
            marked[i-1][j] = True
        # check down
        if i != len(marked) - 1 and not marked[i+1][j]:
            tosearch.append((i+1, j))
            marked[i+1][j] = True

    # add the number of points reached to basins
    basins.append(basin_size)

basins.sort(reverse=True)
print(basins[0]*basins[1]*basins[2])