BOARD_SIZE = 5

class Board:
    def __init__(self, t: list):
        self.nums = t
        self.marked = list()
        for i in range(BOARD_SIZE):
            self.marked.append(list())
            for j in range(BOARD_SIZE):
                self.marked[i].append(False)
    def mark(self, num):
        l = BOARD_SIZE
        for i in range(l):
            for j in range(l):
                if self.nums[i][j] == num:
                    self.marked[i][j] = True
                    return
    def bingo(self):
        l = BOARD_SIZE
        #check vertical bingos
        for i in range(l):
            b = True
            for j in range(l):
                if not self.marked[i][j]:
                    b = False
            if b:
                return True
        #check horizontal bingos
        for i in range(l):
            b = True
            for j in range(l):
                if not self.marked[j][i]:
                    b = False
            if b:
                return True
        #check diagonal bingos (apparently diagonals don't count)
        """
        b = True
        for i in range(l):
            if not self.marked[i][i]:
                b = False
        if b:
            return True
        b = True
        for i in range(l):
            if not self.marked[l-i-1][l-i-1]:
                b = False
        if b:
            return True
        """
        return False
    def score(self, justcalled):
        total = 0
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if not self.marked[i][j]:
                    total += self.nums[i][j]
        return total * justcalled

tocall = []
boards = []
with open("4.txt") as input:
    s = input.readline()
    for tok in s.split(","):
        tocall.append(int(tok))
    while input.readline() != "":
        b = []
        for i in range(BOARD_SIZE):
            row = input.readline().split()
            for j in range(BOARD_SIZE):
                row[j] = int(row[j])
            b.append(row)
        boards.append(Board(b))
    #TODO read 5 lines at a time, create a new board with those lines, append to boards

#part 1
# can't run both in the same execution
"""
done = False
for num in tocall:
    if done:
        break
    for board in boards:
        board.mark(num)
        if board.bingo():
            print(board.score(num))
            done = True
            break
"""

#part 2
for num in tocall:
    for board in boards:
        board.mark(num)
    # check if we are at the last winning board
    if len(boards) == 1 and boards[0].bingo():
        print(board.score(num))
        exit()
    # remove winning boards
    t = []
    for board in boards:
        if not board.bingo():
            t.append(board)
    boards = t