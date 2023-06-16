import pyxel
from lib.config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SQUARE_SIZE,
    ROWS,
    COLS,
    PASS_BTN_X,
    PASS_BTN_Y,
    PASS_BTN_W,
    PASS_BTN_H,
    get_indices
)
from lib.board import Board
from lib.human_player import HumanPlayer
from lib.random_player import RandomPlayer


class Othello:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Pyxel Othello")
        pyxel.mouse(True)
        self.board = Board()
        self.current = 'black'
        self.black_player = HumanPlayer(pyxel, self.board, 'black')
        self.white_player = RandomPlayer(pyxel, self.board, 'white')
        self.winner = None
        self.previous_frame_count = 0
        pyxel.run(self.update, self.draw)

    def change_turn(self):
        """
        手番の変更
        """
        self.current = 'white' if self.current == 'black' else 'black'
        self.winner = self.board.winner()

    def current_player(self):
        """
        現在のプレイヤーを取得
        """
        return self.black_player if self.current == 'black' else self.white_player

    def update(self):
        """
        フレームの更新
        """
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
            return
        if self.winner is not None:
            return
        if self.current_player().move(self.previous_frame_count):
            self.previous_frame_count = pyxel.frame_count
            self.change_turn()

    def draw(self):
        """
        フレームの描画
        """
        # 盤面の描画
        pyxel.cls(0)
        pyxel.rect(0, 0, SCREEN_WIDTH, SCREEN_WIDTH, 3)

        r_idx, c_idx = get_indices(pyxel.mouse_x, pyxel.mouse_y)
        # 配置できる場所だったらマスの色を変える
        if r_idx is not None and c_idx is not None and self.board.can_move(ROWS[r_idx], COLS[c_idx], self.current):
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
        can_pass = self.winner is None and self.board.can_pass(self.current)
        pyxel.rect(PASS_BTN_X, PASS_BTN_Y, PASS_BTN_W, PASS_BTN_H, 9 if can_pass else 13)
        pyxel.text(PASS_BTN_X + 10, PASS_BTN_Y + 3, 'PASS', 7)
        # 現在のプレイヤー表示
        pyxel.text(4, SCREEN_WIDTH + 5, "Black's turn" if self.current == 'black' else "White's turn", 7)
        # ゲーム終了メッセージの描画
        if self.winner:
            color = 'Black' if self.winner == 'black' else 'White'
            pyxel.text(SCREEN_WIDTH // 2 - 34, SCREEN_WIDTH + 5, "{} player wins!".format(color), 14)


if __name__ == "__main__":
    Othello()
