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
        #8方向それぞれの隣あうマスの座標を入れるリスト。隣へ隣へ、と値を更新する。
        direc_list = [[self.ROWS.index(row), self.COLS.index(col)] for _ in range(8)]
        #8方向それぞれのベクトル
        direc_tup = ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1))
        #8方向それぞれに進んで行った時に、rowまたはcolumnにどんな数字または文字が入ったらループを終わるか
        direc_finish_tup = (("1","a"),("1","0"),("1","h"),("0","h"),("8","h"),("8","0"),("8","a"),("0","a"))
        #8方向それぞれに並んでいるコマの色を、中心のコマから近い順に入れていく。中心の隣に何もコマがない時はNone
        direc_turn_list = [[] for _ in range(8)]
        #8面の各方向に進んで行った時に、マスの目に入る値が何だったら終了するのかを示したタプル。0はなんでもいい時。
        #各方向に何枚ひっくり返せるかを入れるリスト
        direc_turn_number = [0] * 8

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

        for i in range(8):
            if direc_list[i] == None:
                direc_turn_list[i] = None
                pass
            else:
                #8方向それぞれについて、端に行くまで
                now_row = 0
                now_col = 0
                for j in range(8):
                    now_row += j * direc_tup[i][0]
                    now_col += j * direc_tup[i][1]
                    if now_row >7 or now_row <0 or now_col >7 or now_col<0:
                        pass
                    else:
                        direc_list[i][0] = self.ROWS[now_row]
                        direc_list[i][1] = self.COLS[now_col]
                        #端に来てないか
                        if direc_list[i][0] == direc_finish_tup[i][0] or direc_list[i][1] == direc_finish_tup[i][1]:
                            pass
                        else:
                            #色情報を入れていく
                            direc_turn_list[i].append(self.RCdic[tuple(direc_list[i])])
        #周囲8方向のマスの石の色が順番に入っているはずなので、あとはTrueとFalseを返す
        for i in range(8):
            if direc_turn_list[i] == None:
                pass
            else:
                for j in range(len(direc_turn_list[i])):
                    if direc_turn_list[i][j] == color:
                        pass
                    else:
                        direc_turn_number[i] += 1
            if direc_turn_number[i] >= 1:
                return True
            else:
                return False
                #色が一緒だったら
    
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
    print(board.can_move("1","a","black"))
