from .Player import Player
from .PlayerType import PlayerType


class Bot(Player):
    def __init__(self, name, id, symbol, difficulty):
        super().__init__(name, id, PlayerType.Bot, symbol)
        self.difficulty = difficulty
