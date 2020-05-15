class Board:
    def __init__(self):
        import itertools
        self.ROWS = ['1', '2', '3', '4', '5', '6', '7', '8']#これをあとで使いたいからselfつける
        self.COLS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
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
        #まずは8方向に存在するマス、石の種類について書いていく
        direc_list = [[] for _ in range(8)]

        direc_tup = ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1))

        if self.row == "1":
            direc_list[0] = None
            direc_list[1] = None
            direc_list[2] = None

        if self.row == "8":
            direc_list[4] = None
            direc_list[5] = None
            direc_list[6] = None

        if self.col == "a":
            direc_list[0] = None
            direc_list[6] = None
            direc_list[7] = None

        if self.col == "h":
            direc_list[2] = None
            direc_list[3] = None
            direc_list[4] = None

        for i in range(8):
            if direc_list[i] == None:
                pass
            else:
                now_direc_tup = direc_tup[i]
                now_row = self.ROWS.index(self.row) + now_direc_tup[0]
                now_col = self.COLS.index(self.col) + now_direc_tup[1]


        return True
    
    def move(self, row, col, color):
        pass

    def can_pass(self, color):
        return True
    
    def winner(self):
        return None

if __name__ == "__main__":
    board = Board()
    print(RCdic)
    print(board.get('5', 'd'))
