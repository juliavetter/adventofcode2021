with open("2.txt") as input:
    depth1 = 0
    x = 0
    depth2 = 0
    aim = 0
    for line in input:
        toks = line.split()
        i = int(toks[1])
        if toks[0] == "forward":
            x += i
            depth2 += aim * i
        elif toks[0] == "down":
            depth1 += i
            aim += i
        elif toks[0] == "up":
            depth1 -= i
            aim -= i
    #part 1
    print(depth1 * x)
    #part 2
    print(depth2 * x)