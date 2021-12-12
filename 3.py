# part 1

lines = 1
bits = []
with open("3.txt") as input:
    line = input.readline()
    for c in line:
        if c == "\n":
            continue
        bits.append(int(c))

    while True:
        line = input.readline()
        if line == "":
            break
        lines += 1
        for i in range(len(line) - 1):
            bits[i] += int(line[i])

    gamma = 0
    epsilon = 0
    for b in bits:
        gamma *= 2
        epsilon *= 2
        if b > lines // 2:
            gamma += 1
        else:
            epsilon += 1
    print("part 1:", gamma * epsilon)

# part 2
co2 = []
ox = []
with open("3.txt") as input:
    for l in input.readlines():
        co2.append(l[:-1]) # remove trailing \n
        ox.append(l[:-1])

for i in range(len(bits)):
    temp = []
    zeros = 0
    ones = 0
    for num in ox:
        if num[i] == '1':
            ones += 1
        else:
            zeros += 1
    if ones >= zeros:
        com = '1'
    else: 
        com = '0'
    for num in ox:
        if num[i] == com:
            temp.append(num)
    ox = temp
    if len(ox) == 1:
        break

for i in range(len(bits)):
    temp = []
    zeros = 0
    ones = 0
    for num in co2:
        if num[i] == '1':
            ones += 1
        else:
            zeros += 1
    if ones >= zeros:
        com = '1'
    else: 
        com = '0'
    for num in co2:
        if num[i] != com:
            temp.append(num)
    co2 = temp
    if len(co2) == 1:
        break
    
print(ox)
print(co2)

print("part 2:")
o = int(ox[0], base=2)
c = int(co2[0], base=2)
print(o,c,o*c)
