class Board:
    def __init__(self):
        import itertools
        self.ROWS = ['1', '2', '3', '4', '5', '6', '7', '8']#これをあとで使いたいからselfつける
        self.COLS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        RCtup = tuple(itertools.product(self.ROWS, self.COLS))
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
        #1:中央マスの周囲8方向に存在するマスの座標を入れるリストを作成。
        #8方向それぞれの隣あうマスの座標を入れるリスト。隣へ隣へ、と値を更新する。
        direc_list = [[] for _ in range(8)]
        
        #8方向それぞれに並んでいるコマの色を、中心のコマから近い順に入れていく。中心の隣に何もコマがない時はNone
        # direc_turn_list = [[] for _ in range(8)]
        #8面の各方向に進んで行った時に、マスの目に入る値が何だったら終了するのかを示したタプル。0はなんでもいい時。
        #各方向に何枚ひっくり返せるかを入れるリスト
        # direc_turn_number = [0] * 8

        #1-1:周囲8方向のマスのうちマスが存在しないところにはNoneを入れる作業
        if row == "1":
            direc_list[0] = None
            direc_list[1] = None
            direc_list[2] = None
        if row == "8":
            direc_list[4] = None
            direc_list[5] = None
            direc_list[6] = None
        if col == "a":
            direc_list[0] = None
            direc_list[6] = None
            direc_list[7] = None
        if col == "h":
            direc_list[2] = None
            direc_list[3] = None
            direc_list[4] = None
        
        #1-2:周囲隣り合っている8方向のマスの座標をdirec_listに入れる
        ## 8方向それぞれのベクトル
        direc_tup = ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1))
        ## now_rowは仮置きの関数で、座標を作るための入れ物

        direc_finish_tup = (("1","a"),("1","0"),("1","h"),("0","h"),("8","h"),("8","0"),("8","a"),("0","a"))

        for i in range(8):
            now_row = self.ROWS.index(row)
            now_col = self.COLS.index(col)
            if direc_list[i] is not None:
                while True:
                    next_row = now_row + direc_tup[i][0]
                    next_col = now_col + direc_tup[i][1]
                    direc_list[i].append([int(next_row),int(next_col)])
                    # print(next_row)
                    # print(next_col)
                    if direc_finish_tup[i][0] == "0":
                        if next_col == self.COLS.index(direc_finish_tup[i][1]):
                            break
                    elif direc_finish_tup[i][1] == "0":
                        if next_row == self.ROWS.index(direc_finish_tup[i][0]):
                            break
                    elif next_row == self.ROWS.index(direc_finish_tup[i][0]) or next_col == self.COLS.index(direc_finish_tup[i][1]):
                        break
                    now_row = next_row
                    now_col = next_col
        print(direc_list[4][0][0])
        board.get(self.ROWS[direc_list[5][0][0]],self.COLS[direc_list[5][0][1]])
        # for i in range(8):
        #     for j in range(len(direc_list[i]):

        #1-3:周囲の座標のそれぞれの色を取ってくる
        # #周囲8方向のマスの石の色が順番に入っているはずなので、あとはTrueとFalseを返す
        # for i in range(8):
        #     if direc_turn_list[i] == None:
        #         pass
        #     else:
        #         for j in range(len(direc_turn_list[i])):
        #             if direc_turn_list[i][j] == color:
        #                 pass
        #             else:
        #                 direc_turn_number[i] += 1
            # if direc_turn_number[i] >= 1:
            #     return True
            # else:
            #     return False
                #色が一緒だったら
    
    def move(self, row, col, color):
        pass

    def can_pass(self, color):
        return True
    
    def winner(self):
        return None

if __name__ == "__main__":
    board = Board()
    # print(RCdic)
    # print(board.get('5', 'd'))
    print(board.can_move("3","d","white"))
