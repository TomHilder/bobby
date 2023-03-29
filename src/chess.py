from .board import Board


class ChessGame():
    
    _game_board: Board = None
    
    def __init__(self) -> None:
        
        self._game_board = Board.default_setup()
        
    @property
    def game_board(self) -> Board:
        return self._game_board