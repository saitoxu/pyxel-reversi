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
        if self.get(row,col) is not None:
            return False
        #1:中央マスの周囲8方向に存在するマスの座標を入れるリストを作成。
        #8方向それぞれの隣あうマスの座標を入れるリスト。隣へ隣へ、と値を更新する。
        direc_list = [[] for _ in range(8)]

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

        #1-3:周囲の座標のそれぞれの色を取ってくる
        color_list = [[] for _ in range(8)]
        for i in range(len(direc_list)):
            if direc_list[i] == None:
                color_list[i] = None
            else:
                for j in range(len(direc_list[i])):
                    color_list[i].append(self.get(self.ROWS[direc_list[i][j][0]],self.COLS[direc_list[i][j][1]]))

        #1-4:周囲の色からそこにコマを置けるかどうかを判断する
        ## 隣り合うマスにコマがあるか、それは置こうとしているコマと反対の色か
        ## 返すことのできるマスの数を記録するリスト
        for cl in color_list:
            if self.turn(color,cl) != 0:
                return True
        return False

    def turn(self,color,color_line):
        if color_line is None:
            return 0
        c_number = 0
        for c in color_line:
            if c is None:
                return 0
            if c != color:
                c_number += 1
            if c == color:
                return c_number
        return 0

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
    print(board.can_move("4","d","white"))
