import random
from .config import (
    ROWS,
    COLS,
    PASS_BTN_X,
    PASS_BTN_Y,
    PASS_BTN_W,
    PASS_BTN_H,
    get_indices
)
from .player import Player


WAIT_FRAME_COUNT = 30

class RandomPlayer(Player):
    def move(self, previous_frame_count):
        """
        手番を進める
        """
        pyxel = self.pyxel
        # 最低30フレームwaitを入れる
        if pyxel.frame_count - previous_frame_count < WAIT_FRAME_COUNT:
            return False
        # パスできる場合はパスする
        if self.board.can_pass(self.color):
            return True
        # ランダムに石を置く
        movable_positions = []
        for row in ROWS:
            for col in COLS:
                if self.board.can_move(row, col, self.color):
                    movable_positions.append((row, col))
        row, col = random.choice(movable_positions)
        self.board.move(row, col, self.color)
        return True
