matchbrac = {'(':')', '[':']', '{':'}', '<':'>'}
revmatchbrac = {')':'(', ']':'[', '}':'{', '>':'<'}

def removelast(l: list, e):
    l.reverse()
    l.remove(e)
    l.reverse()
    return

# try to close the brac in open brac. If failure, return false
def close_brac(openbrac: list, brac: str) -> bool:
    if revmatchbrac[brac] == openbrac[len(openbrac)-1]:
        openbrac.pop()
        return True
    else: 
        openbrac.pop()
        return False

def error_score(line: str) -> int:
    bracval = {')':3, ']':57, '}':1197, '>':25137}
    openbrac = []
    for c in line:
        if c in '([{<':
            openbrac.append(c)
        elif c in ')]}>':
            if not close_brac(openbrac, c):
                return bracval[c]
    return 0

incomplete = []
total = 0
with open("10.txt") as input:
    for line in input.readlines():
        score = error_score(line.strip())
        total += score
        if score == 0:
            incomplete.append(line.strip())
# part 1
print(total)

# part 2
def autocomplete(line: str) -> str:
    openbrac = []
    for c in line:
        if c in '([{<':
            openbrac.append(c)
        elif c in ')]}>':
            close_brac(openbrac, c)
    rest = []
    openbrac.reverse()
    for brac in openbrac:
        rest.append(matchbrac[brac])
    return rest

def autocomplete_score(rest: str) -> int:
    bracval = {')':1, ']':2, '}':3, '>':4}
    score = 0
    for c in rest:
        score *= 5
        score += bracval[c]
    return score

scores = []
for line in incomplete:
    scores.append(autocomplete_score(autocomplete(line.strip())))
scores.sort()
print(scores[len(scores) // 2])