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
        #1:周囲8方向のマスの座標を取ってくるdirec_listを呼び出す
        direc_list = self.make_direc_list(row,col)
        #1-3:周囲の座標とそれぞれの色を辞書型にする
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
        # print(self.RCdic)
        for cl in color_list:
            if self.turn(color,cl) != 0:
                return True
        return False

    #8方向それぞれの隣あうマスの座標を入れるリスト。隣へ隣へ、と値を更新する。
    def make_direc_list(self, row, col):
        direc_list = [[] for _ in range(8)]
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
        return direc_list

    def turn(self,color,color_line): #color_line
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
        if self.can_move(row,col,color) is True:
            RCdic = self.turn_color(row,col,color)
            RCdic[(row,col)] = color
            return RCdic
        else:
            #can_pass(color)
            pass

    def turn_color(self, row, col, color): #マスをひっくり返す関数moveで使う
        which_turn_list = self.which_turn(row,col,color)
        len_wtl = len(which_turn_list)
        for i in range(len_wtl):
            x = str(which_turn_list[i][0]+1)
            y = (which_turn_list[i][1])
            y = self.COLS[y]

            xytuple = (x,y)
            xy_color = self.RCdic[xytuple]
            if xy_color == "black":
                self.RCdic[xytuple] = "white"
            else:
                self.RCdic[xytuple] = "black"
        return self.RCdic


    def which_turn(self, row, col, color): #どのマスをひっくり返すのか判定する関数moveでつかう
        direc_list = self.make_direc_list(row,col)
        
        color_list = [[] for _ in range(8)]
        for i in range(len(direc_list)):
            if direc_list[i] == None:
                color_list[i] = None
            else:
                for j in range(len(direc_list[i])):
                    color_list[i].append(self.get(self.ROWS[direc_list[i][j][0]],self.COLS[direc_list[i][j][1]]))
        which_turn_list = []
        for i in range(len(color_list)):
            cl = color_list[i]
            if self.turn(color,cl) != 0:
                # print(self.turn(color,cl))
                for j in range(self.turn(color,cl)):
                    # print(direc_list[i][j])
                    which_turn_list.append(direc_list[i][j])
                    #8方向の座標の入ったリストから座標だけ抜き取って入れる
        # print(which_turn_list.append(direc_list[0][1]))
        return which_turn_list

    def can_pass(self, color):
        # print(self.RCdic)
        pass_count = 0
        for k,v in self.RCdic.items():
            if v == None:
                which_turn_list = self.which_turn(str(k[0]),str(k[1]),color)
                # print(k,which_turn_list)
                if len(which_turn_list) == 0:
                    pass
                else:
                    pass_count += 1
                    break
            else:
                pass
        if pass_count > 0:
            return False
        else:
            return True

    def winner(self):
        if self.can_pass("white") is True and self.can_pass("black")is True:
            # print(self.RCdic)
            value_list = list(self.RCdic.values())
            # print(value_list)
            count_black = value_list.count("black")
            count_white = value_list.count("white")
            print(count_black)
            print(count_white)
            if count_white > count_black:
                return "white"
            else:
                return "black"
        else:
            return None

if __name__ == "__main__":
    board = Board()
    # print(board.get('3','d'))
    # print(board.can_move("3","e","black"))
    # print(board.make_direc_list("1","a"))
    # print(board.turn_color("3","e","white"))
    # print(board.which_turn("3","d","black"))
    # print(board.move("3","e","white"))
    # print(board.can_pass("white"))
    print(board.winner())
