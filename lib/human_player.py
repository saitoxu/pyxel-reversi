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


class HumanPlayer(Player):
    def move(self, previous_frame_count):
        """
        手番を進める
        """
        pyxel = self.pyxel
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            r_idx, c_idx = get_indices(pyxel.mouse_x, pyxel.mouse_y)
            if r_idx is not None and c_idx is not None and self.board.can_move(ROWS[r_idx], COLS[c_idx], self.color):
                # 石を置く
                self.board.move(ROWS[r_idx], COLS[c_idx], self.color)
                return True
            elif self.board.can_pass(self.color) and self.__pass_button_pressed():
                # パスする
                return True
        return False

    def __pass_button_pressed(self):
        pyxel = self.pyxel
        x = pyxel.mouse_x
        y = pyxel.mouse_y
        min_x = PASS_BTN_X
        max_x = PASS_BTN_X + PASS_BTN_W
        min_y = PASS_BTN_Y
        max_y = PASS_BTN_Y + PASS_BTN_H
        return pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and x >= min_x and x <= max_x and y >= min_y and y <= max_y
