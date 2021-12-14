rules = dict()
polymer = []
STEPS = 10

with open("14.txt") as input:
    polymer = list(input.readline().strip())
    input.readline() # empty line
    for line in input.readlines():
        i = line[0:2]
        o = line[-2:-1]
        rules[i] = o

for i in range(STEPS):
    tempolymer = []
    tempolymer.append(polymer[0])
    for j in range(len(polymer)-1):
        tempolymer.append(rules[polymer[j] + polymer[j+1]])
        tempolymer.append(polymer[j+1])
    polymer = tempolymer

occurences = dict()
for monomer in polymer:
    occurences.setdefault(monomer, 0)
    occurences[monomer] += 1

least = ('', 1_000_000_000)
most = ('', 0)
for e in occurences.items():
    if e[1] < least[1]:
        least = e
    if e[1] > most[1]:
        most = e
print(most[1] - least[1])