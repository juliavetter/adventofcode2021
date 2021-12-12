#part 1
times1478 = 0
with open("8.txt") as input:
    for line in input.readlines():
        for tok in line.split("|")[1].split():
            if len(tok) == 2 or len(tok) == 4 or len(tok) == 3 or len(tok) == 7:
                times1478 += 1
print(times1478)

#part 2
"""
class DigitTemplate:
    def __init__(self):
        self.segments = ['abcdefg']*7
    def __init__(self, s: str):
        if len(s) != 7 or not s.isalpha():
            raise ValueError("DigitTemplate string must be alpha with length 7")
        else:
            self.segments = s
    def __str__(self) -> str:
        return ' ' + self.segments[0]*4 + ' \n' + (self.segments[1] + ' '*4 + self.segments[2] + '\n')*2 + ' ' + self.segments[3]*4 + ' \n' +  (self.segments[4] + ' '*4 + self.segments[5] + '\n')*2 + ' ' + self.segments[6]*4 + ' '

def dval(digit: str, template: DigitTemplate) -> int:
    activated = [0]*7
    for seg in digit:
        i = template.segments.index(seg)
        activated[i] = 1
    if activated == [0,0,1,0,0,1,0]:
        return 1
    elif activated == [1,0,1,1,1,0,1]:
        return 2
    elif activated == [1,0,1,1,0,1,1]:
        return 3
    elif activated == [0,1,1,1,0,1,0]:
        return 4
    elif activated == [1,1,0,1,0,1,1]:
        return 5
    elif activated == [1,1,0,1,1,1,1]:
        return 6
    elif activated == [1,0,1,0,0,1,0]:
        return 7
    elif activated == [1,1,1,1,1,1,1]:
        return 8
    elif activated == [1,1,1,1,0,1,1]:
        return 9
    elif activated == [1,1,1,0,1,1,1]:
        return 0
    else: 
        raise ValueError("input {0} does not correspond to a valid digit according to template \n{1}".format(digit, template))
"""

# return s1 with all the characters in s2 removed
def strdiff(s1: str, s2: str) -> str:
    t = s1
    for c in s2:
        t = t.replace(c, '')
    return t

# return true iff s1 is a scramble of s2
def stramble(s1: str, s2: str) -> bool:
    l1 = list(s1)
    l1.sort()
    l2 = list(s2)
    l2.sort()
    return l1 == l2
total = 0
with open("8.txt") as input:
    for line in input.readlines():
        nums = ['']*10
        # template = DigitTemplate()
        s = line.split("|")[0].split()
        # use known segment layout to determine which strings correspond to which numbers
        # find 1,4,7,8
        for tok in s:
            if len(tok) == 2:
                nums[1] = tok
            elif len(tok) == 3:
                nums[7] = tok
            elif len(tok) == 4:
                nums[4] = tok
            elif len(tok) == 7:
                nums[8] = tok
        # find 6
        for tok in s:
            if len(tok) == 6:
                # either it's a 6, 9, or 0, but 1 shares only one segment with 6
                if len(strdiff(nums[1], tok)) == 1:
                    nums[6] = tok
        # find 9, 0
        for tok in s:
            if len(tok) == 6 and tok != nums[6]:
                # either it's 9 or 0
                if len(strdiff(nums[4], tok)) == 0:
                    nums[9] = tok
                elif len(strdiff(nums[4], tok)) == 1:
                    nums[0] = tok
        # find 3
        for tok in s:
            if len(tok) == 5 and len(strdiff(tok, nums[7])) == 2:
                nums[3] = tok
        # find 2,5
        for tok in s:
            if len(tok) == 5 and tok != nums[3]:
                if len(strdiff(nums[6], tok)) == 2:
                    nums[2] = tok
                elif len(strdiff(nums[6], tok)) == 1:
                    nums[5] = tok

        val = ''        
        for digit in line.split("|")[1].split():
            digit = digit.strip()
            # total += dval(digit, template)
            for i in range(len(nums)):
                # don't check if nums[i] == digit, check that they have all the same characters
                if stramble(nums[i], digit):
                    val = val + str(i)
                    break
        total += int(val)

print(total)

# test digittemplate
"""
d = DigitTemplate()
d.segments = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(d)
"""