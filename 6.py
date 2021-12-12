MATURITY = 7
DAYS = 256

# naive solution only works up to ~120 days
"""
class Fish:
    school = list()
    def __init__(self, timer: int):
        self.timer = timer
    def age():
        babies = 0
        for fish in Fish.school:
            fish.timer -= 1
            if fish.timer < 0:
                fish.timer = MATURITY - 1
                babies += 1
        for i in range(babies):
            Fish.school.append(Fish(MATURITY + 1))

with open("6.txt") as input:
    for n in input.readline().split(","):
        Fish.school.append(Fish(int(n)))
for i in range(DAYS):
    Fish.age()

print(len(Fish.school))
"""

# school[i] := number of fish with maturity i
school = []
for i in range(MATURITY + 2):
    school.append(0)

def age(school: list):
    mature = school[0]
    # make all fish age
    for i in range(1, len(school)):
        school[i-1] = school[i]
    school[len(school)-1] = 0
    # reset parent maturity
    school[MATURITY-1] += mature
    # add new children
    school[MATURITY+1] += mature

with open("6.txt") as input:
    for n in input.readline().split(","):
        n = int(n)
        school[n] += 1
for i in range(DAYS):
    age(school)

print(sum(school))