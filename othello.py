import pyxel

from lib.board import Board

SCREEN_WIDTH = 240
SCREEN_HEIGHT = 256

SQUARE_SIZE = 30
ROWS = ['1', '2', '3', '4', '5', '6', '7', '8']
COLS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

PASS_BTN_X = 202
PASS_BTN_Y = 242
PASS_BTN_W = 36
PASS_BTN_H = 12

class Othello:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Pyxel Othello")
        pyxel.mouse(True)
        self.board = Board()
        self.current_player = 'black'
        self.winner = None
        pyxel.run(self.update, self.draw)

    def get_indices(self, x, y):
        if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_WIDTH:
            return (None, None)
        return (x // SQUARE_SIZE, y // SQUARE_SIZE)

    def change_turn(self):
        if self.current_player == 'black':
            self.current_player = 'white'
        else:
            self.current_player = 'black'
        self.winner = self.board.winner()

    def pass_button_pressed(self):
        x = pyxel.mouse_x
        y = pyxel.mouse_y
        min_x = PASS_BTN_X
        max_x = PASS_BTN_X + PASS_BTN_W
        min_y = PASS_BTN_Y
        max_y = PASS_BTN_Y + PASS_BTN_H
        return pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and x >= min_x and x <= max_x and y >= min_y and y <= max_y
            

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            r_idx, c_idx = self.get_indices(pyxel.mouse_x, pyxel.mouse_y)
            # 石を置く
            if r_idx is not None and c_idx is not None and self.board.can_move(ROWS[r_idx], COLS[c_idx], self.current_player):
                self.board.move(ROWS[r_idx], COLS[c_idx], self.current_player)
                self.change_turn()
            # パスする
            elif self.board.can_pass(self.current_player) and self.pass_button_pressed():
                self.change_turn()


    def draw(self):
        # 盤面の描画
        pyxel.cls(0)
        pyxel.rect(0, 0, SCREEN_WIDTH, SCREEN_WIDTH, 3)

        r_idx, c_idx = self.get_indices(pyxel.mouse_x, pyxel.mouse_y)
        # 配置できる場所だったらマスの色を変える
        if r_idx is not None and c_idx is not None and self.board.can_move(ROWS[r_idx], COLS[c_idx], self.current_player):
            pyxel.rect(SQUARE_SIZE * r_idx, SQUARE_SIZE * c_idx, SQUARE_SIZE, SQUARE_SIZE, 9)

        # 線の描画
        for i in range(len(ROWS) + 1):
            pyxel.line(SQUARE_SIZE * i, 0, SQUARE_SIZE * i, 240, 0)
            pyxel.line(0, SQUARE_SIZE * i, 240, SQUARE_SIZE * i, 0)

        # 石の描画
        for x, row in enumerate(ROWS):
            for y, col in enumerate(COLS):
                color = self.board.get(row, col)
                if color:
                    code = 0 if color == 'black' else 7
                    pyxel.circ(SQUARE_SIZE * x + SQUARE_SIZE // 2,
                               SQUARE_SIZE * y + SQUARE_SIZE // 2, 12, code)

        # パスボタンの描画
        pyxel.rect(PASS_BTN_X, PASS_BTN_Y, PASS_BTN_W, PASS_BTN_H, 9 if self.board.can_pass(self.current_player) else 13)
        pyxel.text(PASS_BTN_X + 10, PASS_BTN_Y + 3, 'PASS', 7)
        # 現在のプレイヤー表示
        pyxel.text(4, SCREEN_WIDTH + 5, "Black's turn" if self.current_player == 'black' else "White's turn", 7)
        # ゲーム終了メッセージの描画
        if self.winner:
            color = 'Black' if self.winner == 'black' else 'White'
            pyxel.text(SCREEN_WIDTH // 2 - 34, SCREEN_WIDTH + 5, "{} player wins!".format(color), 14)


Othello()
