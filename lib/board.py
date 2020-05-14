class Board:
    def __init__(self):
        import itertools
        ROWS = ['1', '2', '3', '4', '5', '6', '7', '8']
        COLS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        RCtup = tuple(itertools.product(ROWS, COLS))
        RCdic = {}
        for i in RCtup:
            if i == ('4', 'e') or i == ('5', 'd'):
                RCdic[i] = "black"
            elif i == ('4', 'd') or i == ('5', 'e'):
                RCdic[i] = "white"
            else:
                RCdic[i] = None
        self.RCdic = RCdic

    def get(self, row, col):
        self.row = row
        self.col = col
        gettup = (self.row , self.col)
        return self.RCdic[gettup]

    def can_move(self, row, col, color):
        return True
    
    def move(self, row, col, color):
        pass

    def can_pass(self, color):
        return True
    
    def winner(self):
        return None

if __name__ == "__main__":
    board = Board()
    print(board.get('5', 'd'))
