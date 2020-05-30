SCREEN_WIDTH = 240
SCREEN_HEIGHT = 256

SQUARE_SIZE = 30
ROWS = ['1', '2', '3', '4', '5', '6', '7', '8']
COLS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

PASS_BTN_X = 202
PASS_BTN_Y = 242
PASS_BTN_W = 36
PASS_BTN_H = 12

def get_indices(x, y):
    """座標からマスを取得"""
    if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_WIDTH:
        return (None, None)
    return (x // SQUARE_SIZE, y // SQUARE_SIZE)
