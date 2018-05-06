from re import compile


class MinesweeperBoard:
    def __init__(self, board):
        regRow = compile(r'^#[ *]+#$')
        regBorder = compile(r'^#+$')

        # Check for validation
        self.__validateRegex(board[0], regBorder)
        self.__validateRegex(board[-1], regBorder)
        for row in board[1:-1]: self.__validateRegex(row, regRow)

        # Init board
        self.board = [list(row) for row in board]
        self.rows = len(board)
        self.cols = len(board[0])

        if not self.rows == self.cols : raise ValueError('Not a square board')

    def __validateRegex(self, stg, reg):
        if not reg.match(stg): raise ValueError('Invalid input!')

    def build(self):
        for i in range(1, self.rows - 1):
            for j in range(1, self.cols - 1):
                if self.board[i][j] == ' ':
                    cnt = self.__count(i, j)
                    if cnt == 0:
                        stg = ' '
                    else:
                        stg = str(cnt)
                    self.board[i][j] = stg

    def toArray(self):
        return [''.join(row) for row in self.board]

    def __count(self, a, b):
        return sum(1 for j in (b - 1, b, b + 1) for i in (a - 1, a, a + 1) if self.board[i][j] == '*')


def board(inp):
    ms = MinesweeperBoard(inp)
    ms.build()
    return ms.toArray()