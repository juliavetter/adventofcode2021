#part 1

with open("1.txt") as input:
    inc = 0
    last = 100000
    for line in input.readlines():
        if int(line) > last:
            inc += 1
        last = int(line)
    print(inc)


#part 2

with open("1.txt") as input:
    inc = 0
    lines = input.readlines()
    for i in range(3, len(lines)):
        if int(lines[i]) > int(lines[i-3]):
            inc += 1
    print(inc)