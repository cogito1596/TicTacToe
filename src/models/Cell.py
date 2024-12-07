from .CellStatus import CellStatus


class Cell:
    def __init__(self, row, coloumn):
        self.row = row
        self.coloumn = coloumn
        self.player = None
        self.status = CellStatus.Empty
