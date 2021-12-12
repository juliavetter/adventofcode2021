# return the nth triangle number
def triangle(n: int):
    return n * (n + 1) // 2

crabs = []
with open("7.txt") as input:
    for tok in input.readline().split(","):
        crabs.append(int(tok))

crabs.sort()
"""
median = len(crabs) / 2
if median.is_integer():
    print(median)
else:
    # average the two medians
    print(crabs[int(median)] + crabs[int(median) + 1] // 2)
"""
# part 1
bestpos = 0
bestfuel = 1_000_000_000_000
besttripos = 0
besttrifuel = 1_000_000_000_000
for pos in range(crabs[len(crabs)-1]):
    fuel = 0
    trifuel = 0
    for crab in crabs:
        fuel += abs(crab-pos)
        trifuel += triangle(abs(crab-pos))
    if fuel < bestfuel:
        bestpos = pos
        bestfuel = fuel
    if trifuel < besttrifuel:
        besttripos = pos
        besttrifuel = trifuel
print(bestfuel)
print(besttrifuel)