from models.board import Board
from models.GameStatus import GameStatus


class Game:
    def __init__(self, dimensions, players, winning_strategies):
        self.players = players
        self.winning_strategies = winning_strategies
        self.Board = Board(dimensions)
        self.moves = []
        self.winner = None
        self.next_turn = 0
        self.game_status = GameStatus.InProgress
