MAX = 1000
grid1 = []
grid2 = []
for i in range(MAX):
    row1 = []
    row2 = []
    for j in range(MAX):
        row1.append(0)
        row2.append(0)
    grid1.append(row1)
    grid2.append(row2)


with open("5.txt") as input:
    for line in input.readlines():
        l = line.split()
        c1 = l[0].split(",")
        c2 = l[2].split(",")
        x1 = int(c1[0])
        y1 = int(c1[1])
        x2 = int(c2[0])
        y2 = int(c2[1])
        # horizontal
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2)+1):
                grid1[i][x1] += 1
                grid2[i][x1] += 1
        # vertical
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2)+1):
                grid1[y1][i] += 1
                grid2[y1][i] += 1
        # diagonal
        else:
            for i in range(abs(x2-x1)+1):
                #down-right
                if x2 > x1 and y2 > y1:
                    grid2[y1+i][x1+i] += 1
                #up-right
                elif x2 > x1 and y2 < y1:
                    grid2[y1-i][x1+i] += 1
                #down-left
                elif x2 < x1 and y2 > y1:
                    grid2[y1+i][x1-i] += 1
                #up-left
                elif x2 < x1 and y2 < y1:
                    grid2[y1-i][x1-i] += 1

total1 = 0
total2 = 0
for i in range(MAX):
    for j in range(MAX):
        if grid1[i][j] >= 2:
            total1 += 1
        if grid2[i][j] >= 2:
            total2 += 1
#part 1
print(total1)
#part 2
print(total2)