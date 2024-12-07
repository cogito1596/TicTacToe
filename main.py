from controller import GameController
from models import Player, Symbol, BotDifficulty, PlayerType


if __name__ == "__main__":
    gc = GameController()
    dimension = 3
    players = [
        Player(name="jake", id=1, type=PlayerType.Human, symbol=Symbol("X")),
        Player(
            name="Computer",
            id=2,
            type=PlayerType.Bot,
            symbol=Symbol("Y"),
            difficulty=BotDifficulty.Easy,
        ),
    ]
