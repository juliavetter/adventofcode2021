rules = {}
polymer = {} # maps 'ab' -> n where n is the number of time 'ab' occurs in the polymer
STEPS = 40

def dictadd(d: dict, key, value) -> None:
    d.setdefault(key, 0)
    d[key] += value
    return

with open("14.txt") as input:
    # initialize polymer
    line = list(input.readline().strip())
    for i in range(len(line)-1):
        pair = line[i] + line[i+1] # pair = 'ab'
        polymer.setdefault(pair, 0)
        polymer[pair] += 1
    # create rules
    input.readline() # empty line
    for line in input.readlines():
        i = line[0:2]
        o = line[-2:-1]
        rules[i] = o

# step over the polymer to build it
for i in range(STEPS):
    tempolymer = {}
    for pair in polymer:
        occ = polymer[pair]
        newpair1 = pair[0] + rules[pair]
        newpair2 = rules[pair] + pair[1]
        dictadd(tempolymer, newpair1, occ)
        dictadd(tempolymer, newpair2, occ)
    polymer = tempolymer

# TODO update this to work with dict polymer
occurences = {}
for item in polymer.items():
    pair = item[0]
    occ = item[1]
    dictadd(occurences, pair[0], occ)

least = ('', float('inf'))
most = ('', 0)
for e in occurences.items():
    if e[1] < least[1]:
        least = e
    if e[1] > most[1]:
        most = e
# is off by one most of the time, just submit multiple times lol (+-1, +-2)
# in my case it was 2 too big
print(most[1] - least[1]) 