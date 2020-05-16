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
        self.color = color
        direc_list = [[] for _ in range(8)]

        direc_tup = ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1))
        direc_finish_tup = (("1","a"),("1","0"),("1","h"),("0","h"),("8","h"),("8","0"),("8","a"),("0","a"))
        #8面の各方向に進んで行った時に、マスの目に入る値が何だったら終了するのかを示したタプル。0はなんでもいい時。

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
                now_row = self.ROWS.index(self.row) + direc_tup[i][0]
                now_col = self.COLS.index(self.col) + direc_tup[i][1]
                direc_list[i][0] = self.ROWS[now_row]
                direc_list[i][1] = self.COLS[now_col]
                #隣のマスを取ってこれたので、色を調べる
                if RCdic[tuple(direc_list[i])] == self.color:
                    pass
                elif:
                    #端かどうかを調べ、端だったらこの回は終了。端じゃなかったら、恥に行くまでの回数同じことを確認できるはず。


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
    print(board.can_move("1","a"))
