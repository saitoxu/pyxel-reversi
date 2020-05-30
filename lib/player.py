from abc import ABCMeta, abstractmethod


class Player(metaclass=ABCMeta):
    def __init__(self, pyxel, board, color):
        self.pyxel = pyxel
        self.board = board
        self.color = color
    
    @abstractmethod
    def move(self, previous_frame_count):
        """
        手番を進める
        石を置くかパスする場合はTrueを, 何もしない場合はFalseを返す
        自分の手番のフレーム毎に実行される
        """
        return False
