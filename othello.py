import pyxel

from lib.board import Board

SCREEN_WIDTH = 240
SCREEN_HEIGHT = 256


class Othello:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, caption="Pyxel Othello")
        pyxel.mouse(True)
        self.board = Board()
        self.current_player = 'b'
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        print(pyxel.mouse_x)

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        pyxel.blt(61, 66, 0, 0, 0, 38, 16)


Othello()
