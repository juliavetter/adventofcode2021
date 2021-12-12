octo = []

with open("11.txt") as input:
    for line in input.readlines():
        line = line.strip()
        octo.append([])
        for c in line:
            octo[len(octo)-1].append(int(c))

def flash(octo: list, i: int, j: int) -> None:
    n = len(octo) - 1
    octo[i][j] = 0
    # for each adjacent element (including diagonally), increment by one
    "TODO"
    if i > 0: #left
        octo[i-1][j] += 1
    if j > 0: #up
        octo[i][j-1] += 1
    if i < n: #right
        octo[i+1][j] += 1
    if j < n: #down
        octo[i][j+1] += 1
    if i > 0 and j > 0: #up left
        octo[i-1][j-1] += 1
    if j > 0 and i < n: #up right
        octo[i+1][j-1] += 1
    if j < n and i > 0: #down left
        octo[i-1][j+1] += 1
    if j < n and i < n: #down right
        octo[i+1][j+1] += 1

# returns the number of flashes in the step
def step(octo: list) -> int:
    flashes = 0
    already_flashed = []
    for i in range(len(octo)):
        already_flashed.append([])
        for j in range(len(octo[i])):
            already_flashed[i].append(False)
            octo[i][j] += 1
    while True:
        flashed = False
        for i in range(len(octo)):
            for j in range(len(octo[i])):
                if not already_flashed[i][j] and octo[i][j] > 9:
                    flash(octo, i, j)
                    already_flashed[i][j] = True
                    flashed = True
        if not flashed:
            break
    # reset any flashed octopus to 0 energy
    for i in range(len(octo)):
        for j in range(len(octo[i])):
            if already_flashed[i][j]:
                octo[i][j] = 0
                flashes += 1
    return flashes

# number of flashes in a step
flashes = 0
for i in range(100):
    flashes += step(octo)

# part 1
print(flashes)

# part 2
i = 100
while True:
    i += 1
    if step(octo) == len(octo) * len(octo[0]):
        break

print(i)