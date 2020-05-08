class Board:
    def __init__(self):
        pass

    def get(self, row, col):
        return 'white'

    def can_move(self, row, col, color):
        return True
    
    def move(self, row, col, color):
        pass

    def can_pass(self, color):
        return True
    
    def winner(self):
        return None
