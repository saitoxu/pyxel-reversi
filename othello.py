import pyxel

from lib.board import Board

SCREEN_WIDTH = 240
SCREEN_HEIGHT = 256

SQUARE_SIZE = 30
ROWS = ['1', '2', '3', '4', '5', '6', '7', '8']
COLS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

class Othello:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Pyxel Othello")
        pyxel.mouse(True)
        self.board = Board()
        self.current_player = 'black'
        pyxel.run(self.update, self.draw)

    def get_indices(self, x, y):
        if x < 0 or x > SCREEN_WIDTH or y < 0 or y > SCREEN_WIDTH:
            return (None, None)
        return (x // SQUARE_SIZE, y // SQUARE_SIZE)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            row, col = self.get_indices(pyxel.mouse_x, pyxel.mouse_y)
            if row is not None and col is not None:
                print(ROWS[row], COLS[col])

    def draw(self):
        # 盤面の描画
        pyxel.cls(0)
        pyxel.rect(0, 0, SCREEN_WIDTH, SCREEN_WIDTH, 3)

        # TODO: 配置できる場所だったらマスの色を変える
        r_idx, c_idx = self.get_indices(pyxel.mouse_x, pyxel.mouse_y)
        if r_idx is not None and c_idx is not None:
            pyxel.rect(SQUARE_SIZE * r_idx, SQUARE_SIZE * c_idx, SQUARE_SIZE, SQUARE_SIZE, 9)

        # 線の描画
        for i in range(len(ROWS) + 1):
            pyxel.line(SQUARE_SIZE * i, 0, SQUARE_SIZE * i, 240, 0)
            pyxel.line(0, SQUARE_SIZE * i, 240, SQUARE_SIZE * i, 0)

        # TODO: 石の描画
        for x, row in enumerate(ROWS):
            for y, col in enumerate(COLS):
                pass

        # TODO: パスボタンの描画
        # TODO: ゲーム終了メッセージの描画


Othello()
